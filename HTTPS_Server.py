import BaseHTTPServer,SimpleHTTPServer,SocketServer
import cgi
import sys
import socket
import ssl

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

httpd = BaseHTTPServer.HTTPServer(("", PORT),Handler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='../cert.pem', server_side=True)
ip = "127.0.0.1" 
print "Serving at: https://%(interface)s:%(port)s" % dict(interface=ip or "localhost", port=PORT)
httpd.serve_forever()
