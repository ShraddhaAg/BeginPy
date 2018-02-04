from sys import argv

script, input_file = argv

def print_all(f):
    print f.read() #prints the entire content of the file pointer passed

def rewind(f):
    f.seek(0) # takes the positon back to beginning

def print_a_line(line_count, f):
    print line_count, f.readline() # prints a single line from the current position of the position pointer

current_file = open(input_file) # makes a file pointer to acces file

print "First let's print the whole file:\n"

print_all(current_file) # calls the function print_all() to print the entire file

print ("Now let's rewind, kind of like a tape.")

rewind(current_file) # takes the position back to the beginning

print ("Let's print three lines: ")

current_line = 1
print_a_line(current_line, current_file) # calls function print_a_line to print the 1st line

current_line+= 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_file.close()
