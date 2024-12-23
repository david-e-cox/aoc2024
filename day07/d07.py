#!/usr/bin/python3

import itertools
import math

# Read input file
#f=open('example.txt')
f=open('input.txt');
lines = f.read().splitlines();
f.close()

partA = 0
partB = 0

def doCalc(opsList,inVals):
    outVal = inVals[0]
    cnt=0
    for val in inVals[1:]:
        if opsList[cnt]=='*':
            outVal *=val
        elif opsList[cnt]=='+':
            outVal +=val
        elif opsList[cnt]=='|':
            outVal = int(str(outVal)+str(val))
        cnt+=1
    return(outVal)
            

def tryAllOpsA(outVal,inVals):
    ops=["*","+"]
    for opsList in itertools.product(ops,repeat=len(inVals)-1):
        calVal = doCalc(opsList,inVals)
        if calVal == outVal:
            return(True)
    return(False)

def tryAllOpsB(outVal,inVals):
    ops=["*","+","|"]
    for opsList in itertools.product(ops,repeat=len(inVals)-1):
        calVal = doCalc(opsList,inVals)
        if calVal == outVal:
            return(True)
    return(False)


for line in lines:
    ab = line.split(':')
    outVal = int(ab[0])
    inVals = [int(x) for x in ab[1].split()]

    if tryAllOpsA(outVal,inVals):
        partA+=outVal

    if tryAllOpsB(outVal,inVals):
        partB+=outVal
        
print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))



