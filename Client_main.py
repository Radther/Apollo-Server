import urllib
import os
import ftplib
import socket

# urllib.urlretrieve("http://10.0.74.92:8000/Files.txt", "listoffiles.txt")
# print open("listoffiles.txt", 'r').read()
# connecting = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting.connect((,8000))


directory = []

try:
    directory = ftp.nlst()
except ftplib.error_perm, resp:
    if str(resp) == "550 No directory found":
        print "No directory in this directory"
    else:
        raise

for f in directory:
    print f



# directory = os.listdir("http://10.0.74.92:8000/")


file1 = raw_input("What file do you want?")
name = raw_input("What do you want it to be called?")

try:
	urllib.urlretrieve("http://10.0.74.92:8000/%s" %file1, name)
	os.system("open "+name)
except urllib.HTTPError:
	print "Try again"
# urllib.urlretrieve("http://88.109.92.229:8000/%s" %file1, name)
# print open("som.jpg", 'r')
# os.system("open "+"som.jpg")