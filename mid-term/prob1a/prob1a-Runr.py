import time



lowerAlphaB = "abcdefghijklmnopqrstuvwxyz"
lowerAlpha = list(set(lowerAlphaB))


with open('sawyer-ascii.txt', 'r') as myFile:
	myTextIn = myFile.read()
	
	myFile.close()
	

myTexts = []
myTexts.append(myTextIn)

#charDict = ''.join(str(x) for x in myTextIn)
myCharDict = list(set(myTextIn))

myDicts = []
myDicts.append(myCharDict)

myText1 = myTextIn.lower()
myTexts.append(myText1)

myDict1 = list(set(myText1))
myDicts.append(myDict1)

myDict2 = list(set(myDict1)^set(lowerAlpha))
myDicts.append(myDict2)

myText2 = myText1
for x in myDict2:
	myText2 = myText2.replace(x, '')
	
myTexts.append(myText2)

if (len(myDicts) == len(myTexts)):
	topCTR = len(myDicts)
	for i in range(topCTR):
		print(len(myDicts[i]))
		print(len(myTexts[i]))
		print('\n')
	

#myDicts.append(lowerAlpha)
