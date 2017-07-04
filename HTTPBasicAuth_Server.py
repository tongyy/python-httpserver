import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import sys
import base64

key = ""

class AuthHandler(SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print(self.headers)
        global key
        ''' Present frontpage with user authentication. '''
        if self.headers.getheader('Authorization') == None:
            self.do_AUTHHEAD()
            self.wfile.write('no auth header received')
            pass
        elif self.headers.getheader('Authorization') == 'Basic '+key:
            SimpleHTTPRequestHandler.do_GET(self)
            pass
        else:
            self.do_AUTHHEAD()
            self.wfile.write(self.headers.getheader('Authorization'))
            self.wfile.write('not authenticated')
            pass

    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        print(body)
        print(self.headers)
        global key
        ''' Present frontpage with user authentication. '''
        if self.headers.getheader('Authorization') == None:
            self.do_AUTHHEAD()
            self.wfile.write('no auth header received')
            pass
        elif self.headers.getheader('Authorization') == 'Basic '+key:
            SimpleHTTPRequestHandler.do_GET(self)
            pass
        else:
            self.do_AUTHHEAD()
            self.wfile.write(self.headers.getheader('Authorization'))
            self.wfile.write('not authenticated')
            pass
def test(HandlerClass = AuthHandler,
         ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    if len(sys.argv)<3:
        print "usage HTTPBasicAuthServer.py [port] [username:password]"
        sys.exit()
    key = base64.b64encode(sys.argv[2])
    test()
