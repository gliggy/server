#!/bin/env python3

#!/usr/bin/env python3

import os
import glob

# set workdir
workdir = "./leo/comics"

"""
#list all dirs
lstdir = ["."]
for dirs in os.walk(workdir):
    lstdir.append(dirs[0])
dirs = lstdir
#print(dirs)

# check if dir function
def isdir(file, dir_file):
    if file.startswith(workdir + dir_file):
        return True
    else:
        return False

# lister function: lists files and dirs
def lister(file):
    if os.path.isfile(file):
        return file
    files = glob.glob(file + "/*")
    return [file, [lister(f) for f in files]]

# construct list
def liststyle(file):
    if type(file) is not list:
        rfile = os.path.relpath(file, start = workdir)
        return "<li><a href='{}'>{}</a></li>\n".format(rfile, rfile)
    dir1 = file[0]
    part = "<li><span class='caret'>{}/</span>\n".format(os.path.relpath(dir1, start = workdir))
    part += "<ul class='nested'>\n"
    part += "".join(liststyle(f) for f in file[1])
    part += "</ul>\n"
    return part
"""

comic = "<!DOCTYPE html>\n<html>\n<head>\n<title>COMICS</title>\n<link rel='stylesheet' type='text/css' href='comic-style.css' />\n<link rel='stylesheet' type='text/css' href='/style.css' />\n</head>"
comic += "<body>"
comic += 
<div>
<br>
<ul class="comicButtons">
<li><a href="/1/">|◀</a></li>
<li><a rel="prev" href="{}" accesskey="p">◀ Prev</a></li>
<li><a href="{}">Random</a></li>
<li><a rel="next" href="{}" accesskey="n">Next ▶</a></li>
<li><a href="comics/">▶|</a></li>
</ul>
<br>
<img src='imgs/{}.png' alt='{}' class='comic'>
<br>
<ul class="comicButtons">
<li><a href="/1/">|◀</a></li>
<li><a rel="prev" href="{}" accesskey="p">◀ Prev</a></li>
<li><a href="{}">Random</a></li>
<li><a rel="next" href="{}" accesskey="n">Next ▶</a></li>
<li><a href="comics/">▶|</a></li>
</ul>
<br>
</div>
lst += "</body>"
with open(workdir + "/sitemap.html", "w") as f:
    f.write(lst)
