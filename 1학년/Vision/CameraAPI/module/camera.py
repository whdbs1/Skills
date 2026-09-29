import pyrealsense2 as rs
import numpy as np
import cv2

# 피드백 주신 화면 기준, 겹침과 깜빡임이 잡힌 최종 HSV 고정값
COLOR_RANGES = {
    "Red": [
        ([0,   70,  60],  [12,  255, 255]),
        ([165, 70,  60],  [180, 255, 255])
    ],
    "Blue": [
        ([100, 70,  60],  [130, 255, 255])
    ],
}

COLOR_BGR = {
    "Red":  (0, 0, 255),
    "Blue": (255, 0, 0),
}

_prev_detected = []
_prev_boxes = {}  # 구조: { label: [(x, y, w, h), ...] }

def _nms(boxes, overlap=0.3):
    if len(boxes) == 0: return []
    boxes = sorted(boxes, key=lambda b: b[2]*b[3], reverse=True)
    keep = []
    for box in boxes:
        x1, y1, w1, h1 = box
        dominated = False
        for kx, ky, kw, kh in keep:
            ix = max(x1, kx)
            iy = max(y1, ky)
            iw = min(x1+w1, kx+kw) - ix
            ih = min(y1+h1, ky+kh) - iy
            if iw > 0 and ih > 0:
                inter = iw * ih
                union = w1*h1 + kw*kh - inter
                if inter / union > overlap:
                    dominated = True
                    break
        if not dominated:
            keep.append(box)
    return keep

def _update_and_smooth_boxes(current_boxes, dist_threshold=15):
    """프레임 간 박스 위치를 보정하여 깜빡임을 잡는 함수"""
    global _prev_boxes
    smoothed_boxes = {}

    for name, boxes in current_boxes.items():
        smoothed_boxes[name] = []
        prev_list = _prev_boxes.get(name, [])

        for (cx, cy, cw, ch) in boxes:
            matched = False
            for (px, py, pw, ph) in prev_list:
                if abs((cx + cw/2) - (px + pw/2)) < dist_threshold and abs((cy + ch/2) - (py + ph/2)) < dist_threshold:
                    nx = int(px * 0.9 + cx * 0.1)
                    ny = int(py * 0.9 + cy * 0.1)
                    nw = int(pw * 0.9 + cw * 0.1)
                    nh = int(ph * 0.9 + ch * 0.1)
                    smoothed_boxes[name].append((nx, ny, nw, nh))
                    matched = True
                    break
            if not matched:
                smoothed_boxes[name].append((cx, cy, cw, ch))

    for name, prev_list in _prev_boxes.items():
        if name not in smoothed_boxes or len(smoothed_boxes[name]) == 0:
            if len(prev_list) > 0:
                smoothed_boxes[name] = prev_list

    _prev_boxes = smoothed_boxes
    return smoothed_boxes

def start():
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    
    profile = pipeline.start(config)
    dev = profile.get_device()
    
    color_sensor = None
    for sensor in dev.query_sensors():
        if sensor.is_color_sensor():
            color_sensor = sensor
            break
            
    if color_sensor is not None:
        if color_sensor.supports(rs.option.enable_auto_exposure):
            color_sensor.set_option(rs.option.enable_auto_exposure, 1)
        if color_sensor.supports(rs.option.enable_auto_white_balance):
            color_sensor.set_option(rs.option.enable_auto_white_balance, 1)
        
    # [수정] 트랙바 생성 창 제거완료
    return pipeline

def stop(pipeline):
    pipeline.stop()
    cv2.destroyAllWindows()

def get_frames(pipeline):
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    
    spatial = rs.spatial_filter()
    temporal = rs.temporal_filter()
    hole_filling = rs.hole_filling_filter()
    
    depth_frame = spatial.process(depth_frame)
    depth_frame = temporal.process(depth_frame)
    depth_frame = hole_filling.process(depth_frame)
    
    depth = np.asanyarray(depth_frame.get_data())
    color = np.asanyarray(frames.get_color_frame().get_data())
    return depth, color

def get_distance(depth, x, y):
    return depth[y, x] / 1000.0

def get_center_distance(depth):
    h, w = depth.shape
    s = int(min(h, w) * 0.05)
    cx, cy = w // 2, h // 2
    roi = depth[cy-s:cy+s, cx-s:cx+s]
    valid = roi[roi > 0]
    return float(np.median(valid) / 1000.0) if len(valid) > 0 else 0.0

def _get_min_area(depth):
    if depth is not None:
        dist = get_center_distance(depth)
        return max(300, int(4000 / (dist + 1)))
    return 600

def _get_mask(hsv, name):
    ranges = COLOR_RANGES[name]
    combined_mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
    
    for lower, upper in ranges:
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        combined_mask = cv2.bitwise_or(combined_mask, mask)
    
    kernel = np.ones((7, 7), np.uint8)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, kernel)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN,  kernel)
    return combined_mask

def get_colors(color_image, depth=None):
    global _prev_detected
    blurred = cv2.GaussianBlur(color_image, (9, 9), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    min_area = _get_min_area(depth)
    
    current_boxes = {}
    for name in COLOR_RANGES.keys():
        mask = _get_mask(hsv, name)
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        boxes = [cv2.boundingRect(c) for c in cnts if min_area <= cv2.contourArea(c) < 80000]
        boxes = _nms(boxes)
        if boxes: current_boxes[name] = boxes

    smoothed = _update_and_smooth_boxes(current_boxes)

    all_cnts = []
    for name, boxes in smoothed.items():
        for x, y, w, h in boxes:
            all_cnts.append((x, y, name))

    all_cnts.sort(key=lambda c: (c[1], c[0]))
    result = [label for x, y, label in all_cnts]
    
    if len(result) == 0: result = _prev_detected
    else: _prev_detected = result
    return result

def show_depth(depth):
    img = cv2.applyColorMap(cv2.convertScaleAbs(depth, alpha=0.05), cv2.COLORMAP_JET)
    h, w = img.shape[:2]
    s = int(min(h, w) * 0.05)
    cx, cy = w // 2, h // 2
    dist = get_center_distance(depth)
    text = "{:.2f}m".format(dist) if dist > 0 else "N/A"
    cv2.rectangle(img, (cx-s, cy-s), (cx+s, cy+s), (255, 255, 255), 2)
    cv2.putText(img, text, (cx-s, cy-s-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow("Depth", img)

def show_colors(color_image, depth=None):
    blurred = cv2.GaussianBlur(color_image, (9, 9), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    result = color_image.copy()
    min_area = _get_min_area(depth)
    
    # [수정] 트랙바 값 획득 및 Debug Mask 생성/출력 코드 완전 제거 완료

    current_boxes = {}
    for name in COLOR_RANGES.keys():
        mask = _get_mask(hsv, name)
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        boxes = [cv2.boundingRect(c) for c in cnts if min_area <= cv2.contourArea(c) < 80000]
        boxes = _nms(boxes)
        if boxes: current_boxes[name] = boxes

    smoothed = _update_and_smooth_boxes(current_boxes)

    for name, boxes in smoothed.items():
        bgr = COLOR_BGR.get(name, (255, 255, 255))
        for x, y, w, h in boxes:
            cv2.rectangle(result, (x, y), (x+w, y+h), bgr, 2)
            cv2.putText(result, name, (x, y-8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, bgr, 2)

    cv2.imshow("Color", result)