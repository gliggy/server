#!/usr/bin/env python3

&quot;&quot;&quot;
Very simple HTTP server in python (Updated for Python 3.7)

Usage:

    ./dummy-web-server.py -h
    ./dummy-web-server.py -l localhost -p 8000

Send a GET request:

    curl http://localhost:8000

Send a HEAD request:

    curl -I http://localhost:8000

Send a POST request:

    curl -d &quot;foo=bar&amp;bin=baz&quot; http://localhost:8000

This code is available for use under the MIT license.

----

Copyright 2021 Brad Montgomery

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.    

&quot;&quot;&quot;
import argparse
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import base64

os.system(&quot;tree leo/ &gt; leo/list.txt&quot;)

class S(BaseHTTPRequestHandler):
    def _set_headers(self, type, status):
        self.send_response(status)
        self.send_header(&quot;Content-type&quot;, type)
        self.send_header(&quot;X-Content-Type-Options&quot;, &quot;nosniff&quot;)
        self.end_headers()

#    def _document(self, document):
#        #This just generates a document
#        content = &quot;{}&quot;.format(document)
#        # &quot;&lt;html&gt;&lt;head&gt;&lt;title&gt;{1}&lt;/title&gt;&lt;/head&lt;body&gt;&lt;h1&gt;{0}&lt;/h1&gt;&lt;h2&gt;Date is {2}&lt;/h2&gt;&lt;/body&gt;&lt;/html&gt;&quot;.format(message, title, today)
#        return content.encode(&quot;utf-8&quot;)  # NOTE: must return a bytes object!

    def do_GET(self):
        # check if file
        path = &quot;./leo/{}&quot;.format(self.path)
        relpath = os.path.relpath(path)
        is_file = os.path.isfile(relpath)
        # which html to serve, perhaps other data types in the future...
        # plain text list
        plain_text = [&quot;c&quot;,&quot;c++&quot;,&quot;com&quot;,&quot;cc&quot;,&quot;conf&quot;,&quot;cxx&quot;,&quot;def&quot;,&quot;f&quot;,&quot;f90&quot;,&quot;for&quot;,&quot;g&quot;,&quot;h&quot;,&quot;hh&quot;,&quot;idc&quot;,&quot;jav&quot;,&quot;java&quot;,&quot;list&quot;,&quot;log&quot;,&quot;lst&quot;,&quot;m&quot;,&quot;mar&quot;,&quot;pl&quot;,&quot;sdml&quot;,&quot;text&quot;,&quot;txt&quot;]

        if not is_file:
            # if it is root, serve index
            if os.path.isdir(relpath):
                self._set_headers(&quot;text/html; charset=utf-8&quot;, 200)
                with open(&quot;{}/index.html&quot;.format(relpath)) as f:
                    content = f.read()#.splitlines()
                    self.wfile.write(&quot;{}&quot;.format(content).encode(&quot;utf-8&quot;))
            elif relpath.endswith(&quot;.teapot&quot;):
                self._set_headers(&quot;text/html; charset=utf-8&quot;, 418)
                self.wfile.write(&quot;&lt;title&gt;TEAPOT&lt;/title&gt;&lt;h1&gt;418 - I AM SHORT AND STOUT&lt;/h1&gt;&quot;.encode(&quot;utf-8&quot;))
            else:
                self._set_headers(&quot;text/html; charset=utf-8&quot;, 404)
                self.wfile.write(&quot;&lt;title&gt;404&lt;/title&gt;&lt;h1&gt;404 - NOT FOUND&lt;/h1&gt;&quot;.encode(&quot;utf-8&quot;))
        else:
            sendReply = False
            if relpath.endswith(&quot;.html&quot;):
                self._set_headers(&quot;text/html; charset=utf-8&quot;, 200)
                type = &quot;text&quot;
                sendReply = True
            if relpath.endswith(&quot;.jpg&quot;):
                self._set_headers(&quot;image/jpg&quot;, 200)
                type = &quot;image&quot;
                sendReply = True
            if relpath.endswith(&quot;.png&quot;):
                self._set_headers(&quot;image/png&quot;, 200)
                type = &quot;image&quot;
                sendReply = True
            if relpath.endswith(&quot;.gif&quot;):
                self._set_headers(&quot;image/gif&quot;, 200)
                type = &quot;image&quot;
                sendReply = True
            if relpath.endswith(&quot;.ico&quot;):
                self._set_headers(&quot;image/x-icon&quot;, 200)
                type = &quot;image&quot;
                sendReply = True
            if relpath.endswith(&quot;.js&quot;):
                self._set_headers(&quot;application/javascript; charset=utf-8&quot;, 200)
                type = &quot;text&quot;
                sendReply = True
            if relpath.endswith(&quot;.css&quot;):
                self._set_headers(&quot;text/css; charset=utf-8&quot;, 200)
                type = &quot;text&quot;
                sendReply = True
            if relpath.rpartition(&#39;.&#39;)[-1] in plain_text:
                self._set_headers(&quot;text/plain; charset=utf-8&quot;, 200)
                type = &quot;text&quot;
                sendReply = True
            if sendReply == True:
                #Open the static file requested and send it
                f = open(relpath, &#39;r&#39; if type == &#39;text&#39; else &#39;rb&#39;) 
                #self.send_response(200)
                #self.send_header(&#39;Content-type&#39;)
                #self.end_headers()
                #print(&quot;HELLO DBG&quot;, type)
                if type == &quot;text&quot;:
                    self.wfile.write(f.read().encode(&quot;utf-8&quot;))
                else:
                    content = f.read()
                    # coded_content = base64.b64encode(content)
                    # print(&quot;coded content&quot;, coded_content)
                    self.wfile.write(content)
                f.close()
            else:
                f = open(relpath)
                self._set_headers(&quot;text/html; charset=utf-8&quot;, 415)
                self.wfile.write(&quot;&lt;h1&gt;415 - Unsupported Media Type&lt;/h1&gt;&lt;pre&gt;{}&lt;/pre&gt;&quot;.format(f.read()).encode(&quot;utf-8&quot;))
        print (relpath)
        now = datetime.now()

        # dd/mm/YY H:M:S
        dt_string = now.strftime(&quot;%d/%m/%Y %H:%M:%S&quot;)
        os.system(&quot;echo &#39;GET {0} at {1}&#39; &gt;&gt; log.txt&quot;.format(relpath, dt_string))
    
    def do_HEAD(self):
        self._set_headers(&quot;text/html&quot;, 200)

    def do_POST(self):
        # Doesn&#39;t do anything with posted data
        content_length = int(self.headers[&#39;Content-Length&#39;]) # &lt;--- Gets the size of data
        post_data = self.rfile.read(content_length) # &lt;--- Gets the data itself
        self._set_headers(&quot;text/html; charset=utf-8&quot;)
        self.wfile.write(self._document(&quot;&lt;html&gt;&lt;body&gt;&lt;p&gt;POST!&lt;/p&gt;&lt;p&gt;{}&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;&quot;.format(post_data).encode(&quot;utf-8&quot;),&quot;POST&quot;))


def run(server_class=HTTPServer, handler_class=S, addr=&quot;localhost&quot;, port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(&quot;Starting httpd server on {0}:{1}&quot;.format(addr,port))
    httpd.serve_forever()



if __name__ == &quot;__main__&quot;:

    parser = argparse.ArgumentParser(description=&quot;Run a simple HTTP server&quot;)
    parser.add_argument(
        &quot;-l&quot;,
        &quot;--listen&quot;,
        default=&quot;localhost&quot;,
        help=&quot;Specify the IP address on which the server listens&quot;,
    )
    parser.add_argument(
        &quot;-p&quot;,
        &quot;--port&quot;,
        type=int,
        default=8000,
        help=&quot;Specify the port on which the server listens&quot;,
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)

