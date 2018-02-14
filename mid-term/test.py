class MyTest(object):
	def __init__(self, val):
		self.val = val
		
	def __lt__(self, other):
		return self.val < other.val
		
	
a = MyTest(2)
b = MyTest(3)

print(a.val)

print(a > b)
