import http.server
import socketserver
import os
import argparse

# Create an argument parser to accept optional port argument
parser = argparse.ArgumentParser(description='Simple HTTP server.')
parser.add_argument('-p','--port', type=int, default=443, help='port to use for the server')

# Parse the arguments
args = parser.parse_args()

# Specify the port you want to use for the server
port = args.port
web_root = "."

# Change the current working directory to the 'wwwroot' folder
os.chdir(web_root)

# Create a custom request handler that serves files with caching disabled
class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

# Create a socket server with the specified port and custom handler
with socketserver.TCPServer(("0.0.0.0", port), NoCacheHandler) as httpd:
    print(f"Serving at http://localhost:{port}")
    httpd.serve_forever()
