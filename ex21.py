print "How old are you?",
age = raw_input()
print "How tall are you?",
height = input()
print "How much do you weigh?",
weight = raw_input()
print "So, you're  %r old, %r tall and %r heavy." % (
age, height, weight)

#raw_input() returns a string, and input() tries to run the input as a Python expression.