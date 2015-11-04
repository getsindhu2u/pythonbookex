from sys import argv
script, user_name = argv
prompt = '> '
print "Hi %s, I'm the %s script." % (user_name, script)
print "what is your name"
name = raw_input(prompt)
print "Where do you work?"
company = raw_input(prompt)
print " I am %s. I work for %s." % (name, company)