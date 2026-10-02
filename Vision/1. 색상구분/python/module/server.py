from http.server import HTTPServer, BaseHTTPRequestHandler
import json

_routes = {}

def on(name, func):
    _routes[name] = func

def on_request(data):
    name = data[0]
    args = data[1:]

    if name in _routes:
        return _routes[name](args)
    return [False, "unknown request"]

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(length).decode('utf-8'))

        result = on_request(data)

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

def start(port=8080):
    HTTPServer(('', port), Handler).serve_forever()