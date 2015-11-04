formatter = "%r%r%r%r"
print formatter %('one','two','three','four')
print formatter %(True, False, True, False)
print formatter %(formatter,formatter,formatter,formatter)
print formatter %("I had this thing","that you can type right","But it dint sing","so I said Good Night")