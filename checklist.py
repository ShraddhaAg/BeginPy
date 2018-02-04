# checklist function
# from sys import argv
from os.path import exists

# i = int(argv[1])

# print("The file ex%d.py exists? %r" %(i, exists("ex%d.py" % i)))

def checklist():
    i = int(raw_input("enter the number of the file you want to check: "))
    print("The file ex%d.py exists? %r" %(i, exists("ex%d.py" % i)))
checklist()
