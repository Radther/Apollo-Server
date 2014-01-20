import urllib
a = urllib.urlretrieve("http://10.0.74.92:8000/hi.txt", "hi.txt")
print a
open("hi.txt")