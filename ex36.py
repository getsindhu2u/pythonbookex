from sys import argv
script, filename = argv

txt = open(filename)
print txt.read()

txt_again = open(filename)
print txt_again.read()


