with open('sawyer-ascii.txt', 'r') as myFile:
	data = myFile.readlines()
	
with open('sawyer-ascii.txt', 'r') as myFile:
	data2 = myFile.read()
	
#print(data)
data3 = ''.join(str(x) for x in data)
#print(data3)
temp = list(set(data3))
print(temp)
print("")
print(len(data3))
print(len(data2))
print(len(data))
