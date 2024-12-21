#!/usr/bin/python3
import re
# Read input file
#f=open('example.txt')
f=open('input.txt')
hlines = f.read().splitlines();
f.close()

partA = 0
partB = 0

# Create buffer characters, appending to input left/right
nullStr=""
for i in range(0,len(hlines[0])):
    nullStr+="."

for i in range(0,len(hlines)):
    hlines[i]=nullStr+hlines[i]+nullStr
    
# transpose input into row orientation (for matching string)
vlines=[]
for j in range(0,len(hlines[0])):
    vlist=[]
    for line in hlines:
        vlist.append(line[j])
    vlines.append("".join(vlist))

# Create positive and negative diagonal matrices
# These align unit slope diagonals along columns
cnt=0
d1lines=[]
d2lines=[]
for line in hlines:
    rcnt=len(hlines[0])-cnt
    d1lines.append(line[cnt:] + nullStr[0:cnt])
    d2lines.append(nullStr[0:cnt] + line[:rcnt])
    cnt+=1

#for line in hlines:
#    print("{}".format(line))
#print("")
#for line in vlines:
#    print("{}".format(line))
#print("")
#for line in d1lines:
#    print("{}".format(line))
#print("")
#for line in d2lines:
#    print("{}".format(line))


# transpose diagonals into row orientation (for matching string)
d1vlines=[]
d2vlines=[]
for j in range(0,len(hlines[0])):
    vlist=[]
    for line in d1lines:
        vlist.append(line[j])
    d1vlines.append("".join(vlist))

    vlist=[]
    for line in d2lines:
        vlist.append(line[j])
    d2vlines.append("".join(vlist))


# Run through rows,columns, plusdiag, minusdiag
for line in hlines:
    match = re.findall(r"XMAS",line)
    partA+=len(match)
    match = re.findall(r"SAMX",line)
    partA+=len(match)

for line in vlines:
    match = re.findall(r"XMAS",line)
    partA+=len(match)
    match = re.findall(r"SAMX",line)
    partA+=len(match)

for line in d1vlines:
    match = re.findall(r"XMAS",line)
    partA+=len(match)
    match = re.findall(r"SAMX",line)
    partA+=len(match)

for line in d2vlines:
    match = re.findall(r"XMAS",line)
    partA+=len(match)
    match = re.findall(r"SAMX",line)
    partA+=len(match)

#Arggg... no benefit from the partA approach, direct search below
for i in range(0,len(hlines)-2):
    for j in range(2,len(hlines[0])):
        localDiag1 = hlines[i][j-2] + hlines[i+1][j-1] + hlines[i+2][j]
        localDiag2 = hlines[i][j]  +  hlines[i+1][j-1] + hlines[i+2][j-2]
        if re.search(r"SAM|MAS",localDiag1) and re.search(r"SAM|MAS",localDiag2):
            partB+=1
            

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


