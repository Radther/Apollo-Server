import urllib
import os
from HTMLParser import *
from Tkinter import *

gui = Tk()
gui.geometry("450x450")


def getFile(self, fileName):
	urllib.urlretrieve("http://10.0.74.25:8000/%s" %fileName, fileName)
	os.system("open "+fileName)


class getFiles(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag =='a':
            for key, value in attrs:
                if key == 'href':
                    filelist.append(value)
directory = 'http://10.0.74.25:8000/'
files = urllib.urlopen(directory).read()
parser = getFiles()
filelist = []
parser.feed(files)

row = 1
for files in filelist:
	button = (Button(gui, text = files, command = lambda files = files: getFiles(files)).pack())






# file1 = raw_input("What file do you want?")
# name = raw_input("What do you want it to be called?")