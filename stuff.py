
        sendReply = False
        if relpath.endswith(".html"):
            self._set_headers("text/html; charset=utf-8", 200)
            sendReply = True
        if relpath.endswith(".jpg"):
            self._set_headers("image/jpg", 200)
            sendReply = True
        if relpath.endswith(".gif"):
            self._set_headers("image/gif", 200)
            sendReply = True
        if relpath.endswith(".js"):
            self._set_headers("application/javascript; charset=utf-8", 200)
            sendReply = True
        if relpath.endswith(".css"):
            self._set_headers("text/css; charset=utf-8", 200)
            sendReply = True
        if relpath.endswith in plain_text:
            self._set_headers("text/plain; charset=utf-8", 200)
            sendReply = True
        if sendReply == True:
            #Open the static file requested and send it
            f = open(relpath) 
            #self.send_response(200)
            #self.send_header('Content-type')
            #self.end_headers()
            self.wfile.write(f.read())
            f.close()
        else:
            self._set_headers("text/plain; charset=utf-8", 415)
            self.wfile.write("415: Unsupported Media Type, may add support later.".encode("utf-8"))
	
				
				
        # if it _is_ a file...
            # TEXT SECTION
            ext = relpath.rpartition('.')[-1]
            if ext == "html":
                self._set_headers("text/html; charset=utf-8", 200)
                with open(relpath) as f:
                    content = f.read()#.splitlines()
                    self.wfile.write(self._document("{}".format(content)))
            # if plain text
            elif ext in plain_text: 
                self._set_headers("text/plain; charset=utf-8", 200)
                with open(relpath) as f:
                    content = f.read()#.splitlines()
                    self.wfile.write(self._document("{}".format(content)))
            # if css or js
            elif ext == "css" or ext == "js":
                if ext == "css":
                    self._set_headers("text/css; charset=utf-8", 200)
                if ext == "js":
                    self._set_headers("text/js; charset=utf-8", 200)
                with open(relpath) as f:
                    content = f.read()#.splitlines()
                    self.wfile.write(self._document("{}".format(content)))
            # IMAGE SECTION
            elif ext == "ico":
                self._set_headers("image/x-icon", 200)
                self.wfile.write(relpath)

