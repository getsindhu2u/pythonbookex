#this is functions using args

def my_details(*args):
	arg1, arg2, arg3 = args
	print "age: %r, name: %r, height: %r" %(arg1, arg2, arg3)
my_details("23", "Sindhu", "5")