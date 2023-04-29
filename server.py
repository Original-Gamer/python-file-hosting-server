from http.server import *

HOST = 'localhost'
PORT = 2137

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>File Host</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h2>Basic file hosting server or something</h2>", "utf-8"))
        self.wfile.write(bytes("<a href='' download='index.html'>index.html</a>", "utf-8"))
        self.wfile.write(bytes("<br>", "utf-8"))
        self.wfile.write(bytes("<a href='' download='gayporn.jpg'>gayporn.jpg</a>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((HOST, PORT), MyServer)
    print(f"Server started at {HOST}, {PORT}.")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print(f"Server stopped.")