#!/usr/bin/env python3.5

import os
import glob
import argparse
import random


parser = argparse.ArgumentParser()
#parser.parse_args()
parser.add_argument("file", help = "file to display", type = int)    # naming it "file"
#parser.add_argument("place", help = "where in list")    # naming it "file"
args = parser.parse_args()  # returns data from the options specified (file)
#print(args.place)

# set workdir
workdir = "./leo/comics/"
file = args.file
#place = args.place
img = "{}.png".format(file)
#alt = "{}.txt".format(file)
#random = random.randint(0,5)

def buttons():
    to_return = "<ul class='comicButtons'>\n"
    to_return += "<li><a href='/comics/1'>|◀</a></li>\n"
    to_return += "<li><a rel='prev' href='/comics/{}' accesskey='p'>◀ Prev</a></li>\n".format(file - 1)
    to_return += "<li><a href='/comics/random'>Random</a></li>\n"
    to_return += "<li><a rel='next' href='/comics/{}' accesskey='n'>Next ▶</a></li>\n".format(file + 1)
    to_return += "<li><a href='/comics'>▶|</a></li>\n"
    to_return += "</ul>\n<br>\n"
    return(to_return)

if os.path.isfile(workdir + "imgs/" + img):
    script = 0
    real_img = "{}.png".format(file)
    alt = "{}.txt".format(file)
    comic = "<!DOCTYPE html>\n<html>\n<head>\n<title>COMICS</title>\n<link rel='stylesheet' type='text/css' href='/comics/comic-style.css' />\n<link rel='stylesheet' type='text/css' href='/style.css' />\n</head>\n"
    comic += "<body>\n<script>0</script>\n<h1>COMICS</h1>\n<div>\n<br>\n".format(script)
    comic += buttons()
    comic += "<a href='/comics/imgs/{0}'><img src='/comics/imgs/{0}' alt='{1}' title='{2}' class='comic'></a>\n<br>\n".format(real_img,file,alt)
    comic += buttons()
    comic += "</div>\n"
    comic += "<script>{}</script>".format(script)
    comic += "</body>\n"
elif file < 1:
    script = "alert('There are no earlier comics.'); window.location.replace('http://leo.growrows.com/comics/{}');".format(1)
    real_img = "{}.png".format(1)
    alt = "{}.txt".format(1)
    comic = "<!DOCTYPE html>\n<html>\n<head>\n<title>COMICS</title>\n<link rel='stylesheet' type='text/css' href='/comics/comic-style.css' />\n<link rel='stylesheet' type='text/css' href='/style.css' />\n</head>\n"
    comic += "<body>\n<script>0</script>\n<h1>COMICS</h1>\n<div>\n<br>\n".format(script)
    comic += buttons()
    comic += "<a href='/comics/imgs/{0}'><img src='/comics/imgs/{0}' alt='{1}' title='{2}' class='comic'></a>\n<br>\n".format(real_img,file,alt)
    comic += buttons()
    comic += "</div>\n"
    comic += "<script>{}</script>".format(script)
    comic += "</body>\n"
else:
    script = "alert('You have reached the last comic.'); window.location.replace('http://leo.growrows.com/comics/{}');".format(file - 1)
    real_img = "{}.png".format(file - 1)
    alt = "{}.txt".format(file - 1)
    comic = "<!DOCTYPE html>\n<html>\n<head>\n<title>COMICS</title>\n<link rel='stylesheet' type='text/css' href='/comics/comic-style.css' />\n<link rel='stylesheet' type='text/css' href='/style.css' />\n</head>\n"
    comic += "<body>\n<script>0</script>\n<h1>COMICS</h1>\n<div>\n<br>\n".format(script)
    comic += buttons()
    comic += "<a href='/comics/imgs/{0}'><img src='/comics/imgs/{0}' alt='{1}' title='{2}' class='comic'></a>\n<br>\n".format(real_img,file,alt)
    comic += buttons()
    comic += "</div>\n"
    comic += "<script>{}</script>".format(script)
    comic += "</body>\n"

    
print(comic)

