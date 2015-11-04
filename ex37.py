from sys import argv
script, filename = argv

print "we are going to erase the file %r" %filename
print "If you want that , hit CTRL-C (^)"
print "If you want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target_file = open(filename, 'w')

print "Truncating the file/Empties the file"
target_file.truncate()

print "These will be the contents of the file"

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "Now we are writing above lines into the file"

target_file.write(line1)
target_file.write("\n")
target_file.write(line2)
target_file.write("\n")
target_file.write(line3)

print "Now finally close the file"
target_file.close()