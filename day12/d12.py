#!/usr/bin/python3
import numpy as np
from scipy import spatial

def findRegions(garden):
    donePos = []
    plot = set()
    plotList = []
    cropList = []
    for row in range(len(garden)):
        for col in range(len(garden[0])):
            if (row,col) not in donePos:
                plot,donePos = expand(garden,(row,col),set(),donePos)
                plotList.append(plot)
                cropList.append(garden[row][col])

    return(cropList,plotList)

def inRange(garden,donePos,pos):
    if (pos[0],pos[1]) not in donePos and pos[0]>=0 and pos[0]<len(garden) and pos[1]>=0 and pos[1]<len(garden[0]):
        return(True)
    return(False)
    
def expand(garden,pos0,plot,donePos):
    move=[(1,0),(-1,0),(0,1),(0,-1)]
    donePos.append(pos0)
    plot.add(pos0)
    for mv in move:
        pos = (pos0[0]+mv[0], pos0[1]+mv[1])
        if  inRange(garden,donePos,pos) and garden[pos0[0]][pos0[1]] == garden[pos[0]][pos[1]]:
            plot.add((pos[0],pos[1]))
            plot,donePos = expand(garden,(pos[0],pos[1]),plot,donePos)
    
    return(plot,donePos)

def findCorners(plot):
    for loc in plot:
        corners=0
        # Handle corner search as logic on three neighbors, col,row and diag
        # Move between the four sign cases
        for testPos in plot:
            for mv in [1,-1]:
                posR=(testPos[0]+mv, testPos[1])
                posC=(testPos[0],    testPos[1]+mv)
                posD=(testPos[0]+mv, testPos[1]+mv)
                # convex corner
                if (posR not in plot) and (posC not in plot):
                    corners+=1
                # interior corner
                if (posR in plot) and (posC in plot) and (posD not in plot):
                    corners+=1
                    
                posR=(testPos[0]+mv, testPos[1])
                posC=(testPos[0],    testPos[1]-mv)
                posD=(testPos[0]+mv, testPos[1]-mv)

                # convex corner
                if (posR not in plot) and (posC not in plot):
                    corners+=1
                # interior corner
                if (posR in plot) and (posC in plot) and (posD not in plot):
                    corners+=1
        return(corners)

def permLength(plot):
    perm=0
    for testPos in plot:
        neighborCnt=0
        for mv in [(1,0),(-1,0),(0,1),(0,-1)]:
            pos=(testPos[0]+mv[0], testPos[1]+mv[1])
            if  inRange(garden,[],pos) and pos in plot:
                neighborCnt+=1
        perm += 4-neighborCnt
    return(perm)


# Read input file
#f=open('example0.txt')
#f=open('example.txt')
f=open('input.txt');
lines = f.read().splitlines();
f.close()

garden=[]
for line in lines:
    garden.append([])
    for c in line:
        garden[-1].append(c)

partA = 0
partB = 0
        
cropList,plotList = findRegions(garden)

permList=[]
neighList=[]
for plot in plotList:
    permList.append(permLength(plot))

for i in range(0,len(permList)):
#    print("Crop {} has cost metrics: {} * {} | {}".format(cropList[i],len(plotList[i]),permList[i],findCorners(plotList[i])))
    partA += len(plotList[i])*permList[i]
    partB += len(plotList[i])*findCorners(plotList[i])

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))



