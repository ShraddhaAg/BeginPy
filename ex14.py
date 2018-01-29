from sys import argv

script, user_name, surname = argv
prompt = 'Enter now: '

print "Hi %s %s, I'm the %s script." % (user_name, surname, script)
print "I'd like to ask you a few questions."
print "Do you like me %s %s?" % (user_name, surname)
likes = raw_input(prompt)

print "Where do you live %s %s?" % (user_name, surname)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, computer)
