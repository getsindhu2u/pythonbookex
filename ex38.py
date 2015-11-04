from sys import argv
script, filename = argv

txt = open(filename)
print "This is file from previous prog"
print txt.read()
print "Hi"
