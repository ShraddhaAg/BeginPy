# function in python (inbuilt)

round() #rounds the decimal values to integers following rules we studied in school

print # will print strings in " " or ' '
        # will print varaibles (eg print x)
        # will print multiple varianles using + or , (eg print x + y [adds no space between the two strings] or print x,y [adds a space])
        # starting a new print statement means a new line unless the previous ended with a ','
        # we can do mathematical operation to print something (eg print '.' * 10 [it will print '.' 10 times with spaces in between])
        # \n also gives new lines (doesn't work wiht %r)
        # use """ """ triple qoutes to type long lines. ie goes across mutiple lines
        # can use () too. but works without it too in 2.7

raw_input([prompt]) # will just take input from user and return the input as of string type without new line
                    # if prompt is present then it will output [print] the prompt on the screen without a new line and wait for input; the input returned is without the prompt or the new line
                    # advised to use this over input() as input () tries to convert the input as if it is python code

open()  # built-in function
        # used to open files, takes parameter: filename and returns the file as an object

splitwords(<string>)

sorted(list) : Sorts the list

pop(index number) :

range(start, stop, step): inclusive of start
                        #doesn't include stop (as it is made in mind to iterate the list which starts with 0 index value, and doesn't include the last length index)
                            step gives the difference betwwen the two, can be positive or negative integer.


string name.append(<element to be added>): adds a single element to the last
                      much slower than extend for longer lists and tuples otherwise append is faster for small lists
                      a string can be added to a list at the end using this but not extend
string name.extend(<elements to be added>): adds all the elemnts given to the end of the string
                                            faster as it is implemented in c
