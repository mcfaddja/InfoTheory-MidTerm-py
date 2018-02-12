with open('sawyer-ascii.txt', 'r') as myFile:
	data = myFile.read()
	
alphaBet = list(set(data))
print(alphaBet)
