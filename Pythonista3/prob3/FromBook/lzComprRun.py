import lz
import time

#import urllib
import requests


#data0 = request.urlopen("http://www.gutenberg.org/files/10/10.txt").read() # read only 20 000 chars
req0 = requests.get("http://www.gutenberg.org/files/10/10.txt")
data0 = req0.text

#urlText = request.urlopen("http://www.gutenberg.org/files/74/old/sawyr11.txt").read()
reqA = requests.get("http://www.gutenberg.org/files/74/old/sawyr11.txt")
urlTextIn = reqA.text


with open('sawyer-ascii.txt', 'r') as myFile:
	origText = myFile.read()
	
	myFile.close()
	

#origText = "This is some test text in a string because looking at how the program runs and figuring out how to debug it with the entire text of 'Tom Sawyer' is a waste of time, borderline impossible, and probably VERY FUCKING STUPID!!!"


origText = urlTextIn
origText = data0



t0 = time.time()
compTextArr = lz.lzCompr(origText)
t1 = time.time()

#oprint(compTextArr)

formCompText = compTextArr[2]
noFormCompText = compTextArr[1]

tTot = t1 - t0
origTextLEN = len(origText)
formCompTextLEN = len(formCompText)
noFormCompTextLEN = len(noFormCompText)

perCnoF = noFormCompTextLEN / origTextLEN
perCisF = formCompTextLEN / origTextLEN

print('\n')
print('# of characters in original version :  ' + str(origTextLEN))
print('# of characters in formatted compressed version :  ' + str(formCompTextLEN))
print('# of characters in NON-formatted compressed version :  ' + str(noFormCompTextLEN))
print('compression ratio of formatted compressed version :  ' + str(perCisF))
print('compression ratio of NON-formatted compressed version :  ' + str(perCnoF))
print('total runtime :  ' + str(tTot) + ' sec')
print('DONE DONE DONE !!!')
print('\n')

#print(compTextArr[0])
#print(formCompText)
