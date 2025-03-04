# api/hello.py

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')  # Change to JSON
        self.end_headers()
        response_data = {"message": "Hello from Python Vercel Function!"} # Create JSON object.
        self.wfile.write(bytes(str(response_data), "utf-8")) # Send JSON object.
        return

    def do_POST(self): # Add post example.
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_data = {"message": "POST request received", "data": post_data.decode("utf-8")}
        self.wfile.write(bytes(str(response_data), "utf-8"))
        return