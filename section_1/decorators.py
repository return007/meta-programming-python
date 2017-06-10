from init import *

###########################################################################################################
#				MAKING DECORATORS FOR METHODS IN PYTHON
###########################################################################################################

# We are creating debug decorator for methods
# Just write @debug on top of methods and u r good to go

def debug(func):
	#func is the input function that has to be wrapped
	def wrapper(*args, **kwargs):
		print func.__name__
		return func(*args, **kwargs)
	return wrapper

def debug_with_param(prefix=''):
	def debug(func):
		def wrapper(*args, **kwargs):
			print str(prefix)+str(func.__name__)
			return func(*args, **kwargs)
		return wrapper
	return debug


# vars(class) :: gives a dictionary of method names and their types 
# .items() :: makes a dictionary iterable for key, value pair
# callable(method) would check if it is method or not
# setattr() sets the value of any attribute for any function, class, etc... 

def debugmethods(cls):
	for k,v in vars(cls).items():
		if callable(v):
			setattr(cls, k, debug(v))
	return cls
