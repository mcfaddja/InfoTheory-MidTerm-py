import math



removeUs = ['\n', ' ', '"', ':', '>', '&', '*', '.', '~', '!', '%', ')', '-', ']', '$', '(', '<', ',', '@', ':', '#', '?', "'", '+', '/', '[', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
removeUs2 = ''.join(str(x) for x in removeUs)

letters = ['abcdefghijklmnopqratuvwxyz']
letters = ''.join(str(x) for x in letters)
letters2 = list(letters)
print(letters2)


print(removeUs2)
with open('sawyer-ascii.txt', 'r') as myfile:
	data = myfile.read()
	
for x in removeUs:
	data2 = data.replace(x, '')

data2 = data2.lower()
	
#print(data)

print(len(data))

counts = []
for x in letters2:
	counts.append(data2.count(x))
	
	
print(counts)
total = sum(counts)
print(total)

freqs = []
for x in counts:
	freqs.append(x / total)
print(freqs)

entropyTOT = 0
for x in freqs:
	entropyTOT = entropyTOT - x * math.log2(x)
	
print(entropyTOT)
