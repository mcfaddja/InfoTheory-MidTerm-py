import time


with open('sawyer-ascii.txt', 'r') as myFile:
	textIn = myFile.read()
	
	myFile.close()


#textIn = "This is some test text in a string"


t0 = time.time()

dictSize = 256
myDict = {chr(i): i for i in range(1,dictSize)}

myAns = []

word = ''
for char in textIn:
	wordNchar = word + char
	
	if wordNchar in myDict:
		word = wordNchar
	else:
		myAns.append(str(myDict[word]))
		
		myDict[wordNchar] = dictSize
		dictSize += 1
		
		word = char
		

if word:
	myAns.append(str(myDict[word]))
	
	
myRet = ''
for row in myAns:
	myRet += row + ','
	
myRet = myRet[:(len(myRet)-1)]


t1 = time.time()

#print(myAns)
print(myRet)
print(len(myRet) / len(textIn))

tTot = t1 - t0
print(tTot)
