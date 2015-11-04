from sys import argv
script, filename = argv

txt = open(filename)
print "My file is %r" %filename
print txt.read()

