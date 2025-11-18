import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

DELAY_SECONDS = 1.5  # change this

class SlowHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        time.sleep(DELAY_SECONDS)
        super().do_GET()

if __name__ == "__main__":
    server = ThreadingHTTPServer(("localhost", 8000), SlowHandler)
    print(f"Serving on http://localhost:8000 with {DELAY_SECONDS}s delay")
    server.serve_forever()
