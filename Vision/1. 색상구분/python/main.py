import module.server as server
import module.camera as cam
import threading
import cv2

pipeline = cam.start()

def get_distance(args):
    depth, color = cam.get_frames(pipeline)
    return [True, cam.get_center_distance(depth)]

def get_xy_distance(args):
    depth, color = cam.get_frames(pipeline)
    return [True, cam.get_distance(depth, args[0], args[1])]

def get_colors(args):
    depth, color = cam.get_frames(pipeline)
    return [True, cam.get_colors(color, depth)]

def stop_camera(args):
    cam.stop(pipeline)
    return [True, "stopped"]

server.on("get_distance",    get_distance)
server.on("get_xy_distance", get_xy_distance)
server.on("get_colors",      get_colors)
server.on("stop_camera",     stop_camera)

# 서버 백그라운드로 실행
threading.Thread(target=server.start, daemon=True).start()

# 카메라 화면 메인스레드에서 표시
while True:
    depth, color = cam.get_frames(pipeline)
    cam.show_depth(depth)
    cam.show_colors(color, depth)

    if cv2.waitKey(1) == 27:  # ESC 종료
        cam.stop(pipeline)
        break
