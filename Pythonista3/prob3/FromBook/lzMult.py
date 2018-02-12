import time



t00 = time.time()


#textIn = "This is some test text in a string"

with open('sawyer-ascii.txt', 'r') as myFile:
	textIn = myFile.read()
	myFile.close()

#textIn = "This is some test text in a string"


t0 = time.time()

#textIn = textIn.lower()

textIn0 = textIn
nCpTOT = 4
for i in range(0, (nCpTOT+1)):
	textIn1 = textIn0
	nCp = i
	if nCp > 0:
		for j in range(1, nCp):
			textIn1 = textIn1 + '\n' + '\n' + '\n' + '\n' + textIn0

	textIn = textIn1
	
	
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
	print('total copies of text: ' + str(nCp+1))
	print('# of chars in input text: ' + str(len(textIn)))
	print('# of chars in unformatted result: ' + str(len(myRes)))
	print('unformatted result compression ratio: ' + str(len(myRes) / len(textIn)))
	print('# of chars in formatted result: ' + str(len(myResult)))
	print('unformatted result compression ratio: ' + str(len(myResult) / len(textIn)))
	
	tTot = t1 - t0
	print('elapsed time: ' + str(tTot) + ' seconds')
	temp = nCp / nCpTOT
	print('We are : ' + str(nCp / nCpTOT) + ' percent done, as we are . . . . ')
	print('DONE with copy ' + str(nCp) + ' of ' + str(nCpTOT) + ' total copies.')
	print('\n')
	

t11 = time.time()	
ttTot = t11 - t00
print('after a TOTAL time of: ' + str(ttTot) + 'seconds, we are FINALLY, ')
print('DONE DONE DONE !!!')
print('\n')
