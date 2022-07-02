import re
import string
import sys


def countpatterninfile():
    regular_expression = input("Enter a regular expression: ")
    found = 0
    fname = "mbox-long.txt"
    fhand = open(fname)

    for line in fhand:
        line = line.rstrip()
        if re.findall(regular_expression, line) != []:
            found += 1
    print ("mbox.txt had " + str(found) + " lines that matched" + regular_expression)

if __name__ == '__main__':
    # this is called a main method
    # This is another way of telling python THIS IS WHERE YOU SHOULD START RUNNING
    # When this is included, python will begin with the code in this block first
    countpatterninfile()

