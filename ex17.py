from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

# print "Copying from %s to %s" %(from_file, to_file)

# in_file = open(from_file)
# indata = in_file.read()

# indata = (open(from_file)).read() # <- Alternate way to write line (8 and 9)

# print "The input file is %d bytes long." % len(indata)

# print "Does the output file exists? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input("> ")

# out_file = open(to_file, 'w+')
# out_file.write(indata)

(open(argv[2], 'w+')).write((open(argv[1])).read())

# print "Alright, all done."

# out_file.close()
