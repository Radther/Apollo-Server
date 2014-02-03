#Import libarys
#urllib is for getting the url and downloading the file and stuff like that
import urllib
#OS is used to run system commands such as opening the file and what not
import os
#HTMLParser is used to the list of files by parsing through the url and getting the files
from HTMLParser import HTMLParser

#This is a counter for adding the number to the files so it's easy to open
counter = 1

#This used to get all the list of files 
class getFiles(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag =='a':
            for key, value in attrs:
                if key == 'href':
                    filelist.append(value)
#This is the URL that you connect to 
directory = 'http://10.0.74.25:8000/'

#This opens the URL and saves it to the var files
files = urllib.urlopen(directory).read()

parser = getFiles()
#This is where the list of files is saved
filelist = []
#This calls the class getFiles and adds the files to the list
parser.feed(files)

#This prints the list of files with the numbers added to them
for files in filelist:
	#Prints the file
	print str(counter) + ". "+files
	#Adds one to the counter
	counter+=1

#This gets the user to type in the number of the file that they want
while True:
	try:
		#Get the number
		fileWant = raw_input("What file do you want? Type in the number")
		#Find that number in the list
		numberFile = filelist[int(fileWant)-1]
		break
	except ValueError:
		print "Type in a number dumbass"

#Find what the user wants it to be called
saveName = raw_input("What do you want it to be called?")

#Grabs the file from the server
def grabFiles(fileWant, saveName):
	#Retreive the file and save it 
	urllib.urlretrieve(directory+"%s" %fileWant, saveName)
	#Open the file first is for make else windows
	if os.name == "posix":
		os.system("open "+saveName)
	else:
		os.system("start "+saveName)

#Call the function that grabs the file
grabFiles(numberFile,saveName)













