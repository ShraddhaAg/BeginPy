from sys import argv

script = argv[0]
first = argv[1]
second = argv[2]
third = argv[3]

print "The script is called:", script
print "You first varaible is:", first
print "Your second variable is:", second
print "Your third variable is:", third

a = raw_input("Are you happy wiht the result? ")
print "%s" % a
