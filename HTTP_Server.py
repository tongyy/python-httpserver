import SimpleHTTPServer
import SocketServer
import cgi
import sys
import socket

PORT = int(sys.argv[1])

def staticHttpServer(req):
        print(req.headers)
	SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(req)

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def do_GET(self):
		staticHttpServer(self)
	def do_POST(self):
                body = self.rfile.read(int(self.headers['Content-Length']))
                print(body)
		staticHttpServer(self)

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)
ip = "127.0.0.1"
print "Serving at: http://%(interface)s:%(port)s" % dict(interface=ip or "localhost", port=PORT)
httpd.serve_forever()
