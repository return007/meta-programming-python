from init import *
###########################################################################################################
#				BASICS OF CLASSES IN PYTHON
###########################################################################################################

class Myclass:
	a = 10
	def __init__(self, b):
		self.b = b

	#Instance Methods of a class have 'self' as argument
	def instance_method(self, param):
		print "My instance variables : ", self.b, "\nWhat I received ", param, "\nThis is now class variable ", self.a

	@classmethod
	def class_method(cls):
		print "class method reporting!!!"

	@staticmethod
	def static_method():
		print "I dont move coz I am static :p"

print_line('#')
print "Basics of classes:: "

obj = Myclass(3)
obj.instance_method(15)
print "class variable:", Myclass.a
obj.class_method()
obj.static_method()

Myclass.class_method()
Myclass.static_method()

print "Also the object structure in python is all dictionary"
print obj.__dict__
print "This listed all the instance variables that were assigned to the object"
print_line('#')