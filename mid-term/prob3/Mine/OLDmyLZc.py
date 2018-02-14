import time


with open('sawyer-ascii.txt', 'r') as myFile:
	textIn = myFile.read()
	
	myFile.close()
	
	
for i in range(1,256):
	temp = chr(i)
	
	print(str(i) + '  ' + temp)
