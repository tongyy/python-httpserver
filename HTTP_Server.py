import SimpleHTTPServer
import SocketServer
import logging
import cgi
import sys
import socket

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

httpd = SocketServer.TCPServer(("", PORT), Handler)
ip = socket.gethostbyname(socket.gethostname())
print "Serving at: http://%(interface)s:%(port)s" % dict(interface=ip or "localhost", port=PORT)
httpd.serve_forever()