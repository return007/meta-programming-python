1. Every value in python has a type.
examples:

type(10) :: <type 'int'>
type('hello') :: <type 'str'>

every type is defined by classes... Here is where things get weird.
type of classes is 'type' 

type(int) :: <class 'type'>

classes are instances of type... This means type is a class.

2. Components of a class:

class Spam(Base):
	def __init__(self, a):
		self.a = a
	def method(self):
		pass

a. Name of class : "Spam"
b. Base class : (Base,)
c. Functions : (__init__,method,)

so to make a new class, we need these parameters...
Spam = type('Spam', (Base,), clsdict) where clsdict is dict of methods in the class

We can create a new 'type' by specifying metaclass=newtype in the () with name of class, and the newtype will be inherited from type class because we would have to use __new__() or else we would have to create our own implementation.

3. Creating a metaclass
A metaclass is a class from which all classes are made. So type is a metaclass. We can create our own meta class by subclassing type class... 

## For python 2 buddies ;)
class mytype(type):
	def __new__(cls, clsname, base, clsdict):
		if clsname == 'Myclass':
			raise TypeError("This is reserved my friend!!!")

		return type.__new__(cls, clsname, base, clsdict)


class Myclass:
	__metaclass__ = mytype
	def method(self):
		pass

Error in creating class :P
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in __new__
TypeError: This is reserved my friend!!!


Metaclasses propogate down heirarchies