import time

def lzCompr(textIn):
	
	myDict = dict()
	myAns = []
	myResult = ''
	
	posCTR = 1
	word = ''
	for char in textIn:
		wordNchar = word + char
		
		if (wordNchar in myDict):
			word = wordNchar
		else:
			myDict[wordNchar] = posCTR
			
			if (len(wordNchar) == 1):
				myAns.append([0, char])
			else:
				anINT = myDict[word]
				myAns.append([anINT, char])
				
			word = ''
			
		posCTR += 1
		
	
	if (word):
		anINT = myDict[word]
		myAns.append([anINT])
		
	
	for row in myAns:
		for col in row:
			myResult = myResult + str(col)
			
			
	return myResult
	
	

with open('sawyer-ascii.txt', 'r') as myFile:
	uncompressed = myFile.read()
	
	#myFile.close()

t0 = time.time()
compressed = lzCompr(uncompressed)
t1 = time.time()

totTime = t1 - t0
print(len(compressed))
print(len(compressed) / len(uncompressed))
print(totTime)

print(compressed)
