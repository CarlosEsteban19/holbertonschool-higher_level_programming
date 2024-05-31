import http.server
import json


class HttpHandler(http.server.BaseHTTPRequestHandler):
    """class derived from BaseHTTPRequestHandler"""

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(info).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b"404 Not Found")


if __name__ == "__main__":
    PORT = 8000
    httpd = http.server.HTTPServer(('', PORT), HttpHandler)
    # Start the server
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
