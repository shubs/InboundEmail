#!/usr/bin/python
import time
import BaseHTTPServer
from pprint import pprint
import urlparse

HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 9000 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_HEAD(s):
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
        def do_GET(s):
                """Respond to a GET request."""
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
                s.wfile.write("<html><head><title>My Parse API Server</title></head><h1>My Parse API Server</h1></html>")
        def do_POST(s):
                """Respond to a POST request."""
                length = int(s.headers['Content-Length'])
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
                s.wfile.write("<html><head><title>cool</title></head>")
                pprint (vars(s))
                 # Extract and print the contents of the POST
                post_data = urlparse.parse_qs(s.rfile.read(length).decode('utf-8'))
                for key, value in post_data.iteritems():
                    print "%s=%s" % (key, value)

                """pprint (vars(s.request))"""

if __name__ == '__main__':
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
        print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
        try:
                httpd.serve_forever()
        except KeyboardInterrupt:
                pass
        httpd.server_close()
        print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)