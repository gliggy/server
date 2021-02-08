#!/usr/bin/env python3.5

import os
import glob

# set workdir
workdir = "./leo/"

# update list (requires tree)
try:
    os.system("tree -F leo/ > ~/leo/list.txt")
except:
    print("tree not found")

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


lst = "<!DOCTYPE html>\n<head>\n<title>SITEMAP</title>\n<link rel='stylesheet' type='text/css' href='bullets.css' />\n<link rel='stylesheet' type='text/css' href='style.css' />\n<meta name='viewport' content='width=device-width, initial-scale=1.0'\n></head>"
lst += "<body>"
lst += "<ul id='sitemap'>\n"
lst += liststyle(lister(workdir))
lst += "</li></ul>\n"
lst += "<script src='list.js'></script>\n"
lst += "</body>"
with open(workdir + "/sitemap.html", "w") as f:
    f.write(lst)