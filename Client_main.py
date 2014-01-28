import urllib
import os
from ftplib import FTP
import socket

# urllib.urlretrieve("http://10.0.74.92:8000/Files.txt", "listoffiles.txt")
# print open("listoffiles.txt", 'r').read()
# connecting = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting.connect((,8000))


from HTMLParser import HTMLParser

class getFiles(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag =='a':
            for key, value in attrs:
                if key == 'href':
                    filelist.append(value)
directory = 'http://10.0.87.20:8000/'
files = urllib.urlopen(directory).read()
parser = getFiles()
filelist = []
parser.feed(files)
for files in filelist:
	print files
# directory = os.listdir("http://10.0.74.92:8000/")


file1 = raw_input("What file do you want?")
name = raw_input("What do you want it to be called?")

try:
	urllib.urlretrieve("http://10.0.87.20:8000/%s" %file1, name)
	os.system("open "+name)
except urllib.HTTPError:
	print "Try again"
# urllib.urlretrieve("http://88.109.92.229:8000/%s" %file1, name)
# print open("som.jpg", 'r')
# os.system("open "+"som.jpg")