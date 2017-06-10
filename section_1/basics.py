from init import print_line

###########################################################################################################
#				CALLING CONVENTIONS IN PYTHON
###########################################################################################################

def func(*args, **kwargs):
	#args would contain all the positional arguments (i.e. func(2,3,4,5,6)) :: args is a tuple
	#kwargs would contain all the keyword arguments (i.e. func(a=12, b=13)) :: kwargs is a dictionary

	print "args: ", args
	print "kwargs: ", kwargs

	print type(args)
	print type(kwargs)

print_line('_')
print "Calling conventions :: "
func(2,3,4,a = 13, b = 16)
print_line('_')

###########################################################################################################
#				CLOSURE OF FUNCTIONS
###########################################################################################################

def construct_func(a,b):
	def func():
		return "I received "+str(a)+" and "+str(b)
	return func

print_line("_")
print "Closure of functions ::"
one = construct_func(1,2)
two = construct_func(3,4)
print one()
print two()
print "\nSome things to notice also: "
print "Address of one: ", one, "Adddress of two: ", two
print "You know what this means :P"
print_line('_')

