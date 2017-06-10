from decorators import *
from init import *

@debug
def sum(a,b):
	return a+b

@debug
def sub(a,b):
	return a-b

print_line('_')
print "Decorators in action:: "
print sum(1,2)
print sub(1,2)
print_line("_")


@debug_with_param(prefix=">>>")
def mul(a,b):
	return a*b

print_line('_')
print mul(2,3)

@debug_with_param()
def div(a,b):
	return a/b

print div(10,2)