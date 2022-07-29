class AA:
	def __init__(self):
		self.test = 0
		
	def foo(self):
		self.__init__()
		
aa = AA()
aa.test = 5
print(aa)
print(aa.test)
aa.foo()
print(aa)
print(aa.test)