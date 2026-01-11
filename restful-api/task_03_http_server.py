from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b"Hello")

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

server = HTTPServer(("localhost", 8000), SimpleAPIHandler)
print("Server running on http://localhost:8000")
server.serve_forever()
