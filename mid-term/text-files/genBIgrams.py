with open('alpha.txt', 'r') as myFile:
	lowerARR = myFile.readlines()
	
for i in range(len(lowerARR)):
	lowerARR[i] = lowerARR[i].replace('\n', '')

print(lowerARR)


lowerLST = ''.join(str(x) for x in lowerARR)

print(lowerLST)

biGrams = []
for x in lowerARR:
	for y in lowerARR:
		biGrams.append(x.join(y))
		
print(26*26)
print(len(biGrams))
