def lzCompr(textIn):
	
	myDict = dict()
	myAns = []
	myResult = ''
	myCompr = ''
	
	posCTR = 1
	word = ''
	for char in textIn:
		wordNchar = word + char
		
		if (wordNchar in myDict):
			word = wordNchar
		else:
			myDict[wordNchar] = posCTR
			posCTR += 1
			
			if (len(wordNchar) == 1):
				myAns.append([0, char])
			else:
				anINT = myDict[word]
				myAns.append([anINT, char])
				
			word = ''
			
		#posCTR += 1
		
	
	if (word):
		anINT = myDict[word]
		myAns.append([anINT])
		
	
	for row in myAns:
		for col in row:
			myResult = myResult + str(col)
			
	
	for row in myAns:
		tst = 0
		
		for col in row:
			if tst = 0:
				myAns = myAns + col + ','
			else:
				myAns = myAns + col + ';'
				
			tst += 1
	
	
	myOut = [myResult, myAns]	
	
	#return myResult
	return myOut
