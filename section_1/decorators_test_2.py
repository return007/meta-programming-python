from decorators import *
from init import *

#Now I have to decorate all the methods of this class, so now we make a decorator for class, which would mean that 

@debugmethods
class NeedToBeDecorated:

	def method1(self):
		pass

	def method2(self):
		pass

	@classmethod
	def cmethod(cls):
		pass

	@staticmethod
	def smethod():
		pass

obj = NeedToBeDecorated()
obj.method1()
obj.method2()

# Important point to note here, this would not work for class and static methods
obj.cmethod()
obj.smethod()