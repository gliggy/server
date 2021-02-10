#!/usr/bin/env python3.5

"""
Very simple HTTP server in python (Updated for Python 3.7)

Usage:

    ./dummy-web-server.py -h
    ./dummy-web-server.py -l localhost -p 8000

This code is available for use under the MIT license.

----

Copyright 2021 Brad Montgomery

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.    

"""
# requirements: argparse, os, http.server, datetime, base64, glob
import argparse
import os
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import base64
import glob


# set workdir
workdir = "./leo/"
absdir = os.path.abspath("leo")

# list site
os.system("./sitemap.py")

# ~~~~~~~~~~~~~~~~~~Handler~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def escape(t):
    """HTML-escape the text in `t`."""
    return (t
        .replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        .replace("'", "&#39;").replace('"', "&quot;")
        )


class S(BaseHTTPRequestHandler):
    def _set_headers(self, type, status):
        self.send_response(status)
        self.send_header("Content-type", type)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

    def do_GET(self):
        # check if file
        path = workdir + self.path
        relpath = os.path.relpath(path)
        abspath = os.path.abspath(path)
        is_file = os.path.isfile(relpath)
        # which html to serve, perhaps other data types in the future...
        # plain text list
        plain_text = ["c","c++","com","cc","conf","cxx","def","f","f90","for","g","h","hh","idc","jav","java","list","log","lst","m","mar","pl","sdml","text","txt","py"]

        if not is_file:
            # if it is root, serve index
            if os.path.isdir(relpath):
                self._set_headers("text/html; charset=utf-8", 200)
                with open("{}/index.html".format(relpath)) as f:
                    content = f.read()
                    self.wfile.write("{}".format(content).encode("utf-8"))
            elif relpath.endswith(".teapot"):
                self._set_headers("text/html; charset=utf-8", 418)
                self.wfile.write("<title>TEAPOT</title><h1>418 - I AM SHORT AND STOUT</h1>".encode("utf-8"))
            elif relpath.startswith("leo/comics/"):
                file = relpath.split("comics/",1)[1]
                #if os.path.isfile("leo/comics/imgs/{}.png".format(file)):
                comic_file = subprocess.run(["./comics.py", "{}".format(file)], stdout=subprocess.PIPE)
                content = comic_file.stdout.decode("utf-8")
                self._set_headers("text/html; charset=utf-8", 200)
                self.wfile.write("{}".format(content).encode("utf-8"))
                """elif os.path.isfile("leo/comics/imgs/{}.png".format(int(file) - 1)):
                    comic_file = subprocess.run(["./comics.py", "{}".format(int(file) - 1)], stdout=subprocess.PIPE)
                    print(int(file) - 1)
                    content = comic_file.stdout.decode("utf-8")
                    self._set_headers("text/html; charset=utf-8", 200) 
                else:
                    self._set_headers("text/html; charset=utf-8", 404)
                    self.wfile.write("<title>404</title><h1>404 - NOT FOUND</h1>".encode("utf-8"))"""
            else:
                self._set_headers("text/html; charset=utf-8", 404)
                self.wfile.write("<title>404</title><h1>404 - NOT FOUND</h1>".encode("utf-8"))
        else:
            sendReply = False
            if relpath == "leo/list.txt":
                self._set_headers("text/html; charset=utf-8", 200)
                type = "list"
                sendReply = True
            if relpath.endswith(".html"):
                self._set_headers("text/html; charset=utf-8", 200)
                type = "text"
                sendReply = True
            if relpath.endswith(".jpg"):
                self._set_headers("image/jpg", 200)
                type = "image"
                sendReply = True
            if relpath.endswith(".png"):
                self._set_headers("image/png", 200)
                type = "image"
                sendReply = True
            if relpath.endswith(".gif"):
                self._set_headers("image/gif", 200)
                type = "image"
                sendReply = True
            if relpath.endswith(".ico"):
                self._set_headers("image/x-icon", 200)
                type = "image"
                sendReply = True
            if relpath.endswith(".js"):
                self._set_headers("application/javascript; charset=utf-8", 200)
                type = "text"
                sendReply = True
            if relpath.endswith(".css"):
                self._set_headers("text/css; charset=utf-8", 200)
                type = "text"
                sendReply = True
            if relpath.rpartition('.')[-1] in plain_text and relpath != "leo/list.txt":
                self._set_headers("text/plain; charset=utf-8", 200)
                type = "text"
                sendReply = True

            if sendReply == True and abspath.startswith(absdir):
                #Open the static file requested and send it
                f = open(relpath, 'r' if type == 'text' or type == 'list' else 'rb') 
                #self.send_response(200)
                #self.send_header('Content-type')
                #self.end_headers()
                #print("HELLO DBG", type)
                if type == "text":
                    self.wfile.write(f.read().encode("utf-8"))
                elif type =="list":
                    self.wfile.write("<title>List</title><pre>{}</pre>".format(f.read()).encode("utf-8"))
                else:
                    content = f.read()
                    # coded_content = base64.b64encode(content)
                    # print("coded content", coded_content)
                    self.wfile.write(content)
                f.close()
            elif sendReply == True and not abspath.startswith(absdir):
                self._set_headers("text/html; charset=utf-8", 403)
                self.wfile.write("<title>403</title><h1>403 - Forbidden</h1>".encode("utf-8"))
            else:
                f = open(relpath)
                self._set_headers("text/html; charset=utf-8", 415)
                self.wfile.write("<h1>415 - Unsupported Media Type</h1><pre>{}</pre>".format(escape(f.read())).encode("utf-8"))
        print (relpath)
        print (os.path.abspath(path))
        now = datetime.now()

        # date
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        #os.system("echo 'GET {0} at {1}' >> log.txt".format(relpath, dt_string))
    
    def do_HEAD(self):
        self._set_headers("text/html", 200)

    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self._set_headers("text/html; charset=utf-8")
        self.wfile.write(self._document("<html><body><p>POST!</p><p>{}</p></body></html>".format(post_data).encode("utf-8"),"POST"))


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print("Starting httpd server on {0}:{1}".format(addr,port))
    httpd.serve_forever()



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)

