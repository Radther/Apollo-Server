import BaseHTTPServer
import os

PORT = 8000

class request(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type','text/html')
		self.end_headers()
		self.wfile.write("Hello World")
		return


server = BaseHTTPServer.HTTPServer(('',PORT),request)
print "server started on port", PORT

server.serve_forever()