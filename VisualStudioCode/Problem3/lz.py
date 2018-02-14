def lzCompr(textIn):
	
	myDict = dict()
	myAns = []
	myResult = ''
	myComp = ''
	
	
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
			
			
	if (word):
		anINT = myDict[word]
		myAns.append([anINT])
		
	
	for row in myAns:
		for col in row:
			myResult = myResult + str(col)
			
	
	for row in myAns:
		tst = 0
		
		for col in row:
			
			if tst == 0:
				myComp = myComp + str(col) + ','
			else:
				myComp = myComp + str(col) + ';'
					
			tst += 1
	
	
	
	myOut = [myAns, myResult, myComp]	
	
	#return myResult
	return myOut
	
	
	


def lzDEcompr(inArray):
	mySize = len(inArray)
	mySize1 = mySize - 1

	myEndSize = len(inArray(mySize - 1))
	
	deCompText = ""

	for i in range(mySize1):
		row = inArray(i)
        
        numNow = row(0)
        charNow = row(1)

        if (numNow == 0):
            deCompText += charNow
        else:
            wordNow = charNow

            while (numNow != 0):
                newRow = inArray(numNow)

                charNow = newRow(1)
                wordNow = charNow + wordNow

                numNow = newRow(0)
            
            deCompText += wordNow
        
    
    row = inArray(mySize1)
    if (myEndSize == 1):
        tmpNum = row(0)

        rowNow = inArray(tmpNum)

        charNow = rowNow(1)
        numNow = rowNow(0)

        if (numNow == 0):
            deCompText += charNow
        else:
            wordNow = charNow

            while (numNow != 0):
                newRowNow = inArray(numNow)

                charNow = newRowNow(1)
                wordNow = charNow + wordNow

                numNow = newRowNow(0)
            
            deCompText += wordNow
        
    else:
        charNow = row(1)
        numNow = row(1)

        if (numNow == 0):
            deCompText += charNow
        else:
            wordNow = charNow

            while (numNow != 0):
                newRowNow = inArray(numNow)

                charNow = newRowNow(1)
                wordNow = charNow + wordNow

                numNow = newRowNow(0)
            
            deCompText += wordNow


    return deCompText
