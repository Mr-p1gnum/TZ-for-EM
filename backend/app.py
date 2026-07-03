import os
from http.server import BaseHTTPRequestHandler, HTTPServer

HEADER = os.environ.get("HEADER", "")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = "Hello from Effective Mobile!"
            if HEADER:
                body += f"\n{HEADER}"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Not Found".encode("utf-8"))

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Server running on port 8080...")
    server.serve_forever()