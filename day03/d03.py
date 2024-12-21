#!/usr/bin/python3
import re
import ast

# Read input file
#f=open('exampleB.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()

partA = 0
for line in lines:
    matches = re.findall(r"mul\((\d+),(\d+)\)",line)
    for vals in matches:
        partA += int(vals[0])*int(vals[1])


partB = 0
mulEnable = True
for line in lines:
    ptr=0
    while ptr<len(line):
        mul  = re.search(r"mul\((\d+),(\d+)\)",line[ptr:])
        if (mul is None):
            # No more mul() statements, program done
            ptr = len(line)
            break
        # Get do/dont in segment leading up to mul()
        do   = re.search(r"do\(\)",line[ptr:ptr+mul.end()])
        dont = re.search(r"don't\(\)",line[ptr:ptr+mul.end()])

        # Corner case, both do and don't before next mul(), obey last
        if do and dont:
            if do.end()>dont.end():
                dont=None
            else:
                do=None

        if dont:
            mulEnable = False

        if do:
            mulEnable = True


        if mulEnable:
            partB += int(mul.group(1))*int(mul.group(2))

        # Increment program pointer
        ptr += mul.end()

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


