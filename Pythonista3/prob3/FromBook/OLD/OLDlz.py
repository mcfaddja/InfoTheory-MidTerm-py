import time




#textIn = "This is some test text in a string"

with open('sawyer-ascii.txt', 'r') as myFile:
	textIn = myFile.read()
	myFile.close()
	
	
#textIn = "This is some test text in a string"



t0 = time.time()


#textIn = textIn.lower()

textIn0 = textIn
nCp = 0
if nCp > 0:
	for i in range(1, nCp):
		textIn0 = textIn0 + '\n' + '\n' + '\n' + '\n' + textIn
	
textIn1 = textIn
textIn = textIn0
textIn0 = textIn1
del(textIn1)


myDict = dict()
myAns = []
myResult = ''
myRes = ''

posCTR = 1
word = ''
for char in textIn:
	wordNchar = word + char
	
	if (wordNchar in myDict):
		word = wordNchar
	else:
		myDict[wordNchar] = posCTR
		posCTR = posCTR + 1
		
		if (len(wordNchar) == 1):
			myAns.append([0, char])
		else:
			anINT = myDict[word]
			myAns.append([anINT, char])
				
		word = ''
	
#print(myDict)
		
	
if (word):
	anINT = myDict[word]
	myAns.append([anINT])
	
#print(myAns)
		
	
for row in myAns:
	i = 0
	for col in row:
		myRes = myRes + str(col)
		
		if i == 0:
			myResult = myResult + str(col) + ','
		else:
			myResult = myResult + str(col) + ';'
			
		i += 1
		

t1 = 	time.time()
#print(myResult[])

#print('\n')
print('total copies of text: ' + str(nCp))
print('# of chars in input text: ' + str(len(textIn)))
print('# of chars in unformatted result: ' + str(len(myRes)))
print('unformatted result compression ratio: ' + str(len(myRes) / len(textIn)))
print('# of chars in formatted result: ' + str(len(myResult)))
print('unformatted result compression ratio: ' + str(len(myResult) / len(textIn)))

tTot = t1 - t0
print('elapsed time: ' + str(tTot) + ' seconds')
print('DONE DONE DONE !!!')
print('\n')
