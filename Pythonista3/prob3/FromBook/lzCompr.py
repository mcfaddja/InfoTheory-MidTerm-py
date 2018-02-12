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
