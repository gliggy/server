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
alt = "{}.txt".format(file)
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

script = 0
#if place == "last":
#    script = "alert('You're at the last comic.');"

comic = "<!DOCTYPE html>\n<html>\n<head>\n<title>COMICS</title>\n<link rel='stylesheet' type='text/css' href='/comics/comic-style.css' />\n<link rel='stylesheet' type='text/css' href='/style.css' />\n</head>\n"
comic += "<body>\n<script>{}</script>\n<h1>COMICS</h1>\n<div>\n<br>\n".format(script)
comic += buttons()
comic += "<img src='/comics/imgs/{}' alt='{}' title='{}' class='comic'>\n<br>\n".format(img,file,alt)
comic += buttons()
comic += "</div>\n"
comic += "</body>\n"

#with open(workdir + "index.html", "w") as f:
#    f.write(comic)
    
print(comic)

