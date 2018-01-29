from sys import argv # tell's python to get the variable argv in the script we are using

script, filename = argv # takes the arguments passed in the argv using terminal and assigns it to different variables

txt = open(filename) # uses the function open to open the file passing the name of the file as a parameter

print "Here's your file %s: " % filename
print txt.read() # the object txt uses its function read() to read the file and whatever is being read is printed on the screen by print

print "Type the filename again:"
file_name =  raw_input("> ")

txt_again = open(file_name)

print txt_again.read()
