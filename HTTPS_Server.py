import BaseHTTPServer,SimpleHTTPServer,SocketServer
import logging
import cgi
import sys
import socket
import ssl

PORT = int(sys.argv[1])

def staticHttpServer(req):
	logging.warning(req.headers)
	SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(req)

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def do_GET(self):
		"do something for GET"
		staticHttpServer(self)
	def do_POST(self):
		"do something for POST"
		staticHttpServer(self)

Handler = ServerHandler

httpd = BaseHTTPServer.HTTPServer(("", PORT),Handler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./cert.pem', server_side=True)
ip = socket.gethostbyname(socket.gethostname())
print "Serving at: https://%(interface)s:%(port)s" % dict(interface=ip or "localhost", port=PORT)
httpd.serve_forever()