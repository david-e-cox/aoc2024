#!/usr/bin/python3

import copy 

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()

partA=0
partB=0

pairs=dict();
pageList=[]
pairMode=True
for line in lines:
    if len(line)==0:
        pairMode=False
        continue
    if (pairMode): # Reading part of file with rule pairs
        keyValue = line.split('|')
        key=int(keyValue[0])
        val=int(keyValue[1])
        # Append rules into value of dictionary
        if key in pairs.keys():
            pairs[key].append(val)
        else:
            pairs[key]=[val]
    else:  # Section of input with page update lists
        pageList.append([int(x) for x in line.split(',')])

        
def checkPredecessors(pairs,pages):
    preSet=[]  # Set of pages that have already been printed, grows as pages are added
    newPages=copy.deepcopy(pages)
    for page in pages:
        preSet.append(page)
        if page in pairs.keys():  # A rule exists for this page
            for val in preSet:  # Check prior printed pages for a violation of the rule
                if val in pairs[page]:
                    goodUpdate=False
                    # Swap two pages to satisfy the rule which was just violated
                    ndx1=newPages.index(val)
                    ndx2=newPages.index(page)
                    newPages[ndx1]=pages[ndx2]
                    newPages[ndx2]=pages[ndx1]
                    # Return False (for valid result) and newPages order
                    return((False,newPages))
    return((True,newPages))

badList=[]
for i in range(0,len(pageList)):
    isValid,newPages = checkPredecessors(pairs,pageList[i])
    if isValid:
        ndx=int(len(pageList[i])/2)
        partA += pageList[i][ndx]
    else:
        badList.append(i)

        
# Process failed pages to return valid page ordering list
for pgNum in badList:
    # Call checkPredecessors, applying fix for rule voilation.  Continue until all rules are satisfied
    isValid,newPages = checkPredecessors(pairs,pageList[pgNum])
    while not isValid:
        isValid,newPages = checkPredecessors(pairs,newPages)

    # Find center point of re-ordered page list and increment partB
    ndx=int(len(newPages)/2)
    partB += newPages[ndx]

    
print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


