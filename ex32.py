the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list:
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %r" % fruit

# also we can go through mixed losts too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first strat with an empty one
elements = [range(0,6)]

# then use the range function to do 0 to 5
#for i in range(0,5):
#    print "Adding %d to the line." % i
    # append is a function that lists understand
    elements.append(i)

#now we can print them out out
for i in elements:
    print "Elemet was: %d" % i
