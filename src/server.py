import os
from http.server import BaseHTTPRequestHandler, HTTPServer

NOTES = ["alpha", "beta", "gamma", "delta"]

# Settings from Kubernetes ConfigMap and Secret
GREETING = os.environ.get("GREETING", "Hello")
API_KEY = os.environ.get("API_KEY", "")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self._send(200, b"ok")

        elif self.path == "/":
            message = f"{GREETING} - notes service"
            self._send(200, message.encode())

        elif self.path == "/notes":
            self._send(200, str(len(NOTES)).encode())

        elif self.path == "/config":
            if API_KEY:
                self._send(200, b"API key configured")
            else:
                self._send(503, b"API key missing")

        else:
            self._send(404, b"not found")

    def _send(self, code, body):
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


def make_server(port):
    return HTTPServer(("0.0.0.0", port), Handler)


if __name__ == "__main__":
    make_server(int(os.environ.get("PORT", "8080"))).serve_forever()
