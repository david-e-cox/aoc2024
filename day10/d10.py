#!/usr/bin/python3
import numpy as np
import copy

def checkMoves(topoMap,loc,path,summit,allTrails):
    path.append(loc)
    world=topoMap.shape

    possibleMoves=[]
    moves=[(0,-1),(1,0),(0,1),(-1,0)]; #North,East,South,West
    for mv in moves:
        onMap=False
        pos = [loc[0]+mv[0], loc[1]+mv[1]]
        if ( pos[0] >= 0 and pos[0] < world[0] and pos[1] >= 0 and pos[1] < world[1] ):
            onMap=True
        if onMap:
            if ( topoMap[pos[0],pos[1]] - topoMap[loc[0],loc[1]] == 1 ):
                possibleMoves.append(mv)

    if len(possibleMoves)==0:
        # Check to see if we reached a summit
        # If so add summit location and pathlog to output sets
        if topoMap[loc[0],loc[1]]==9:
            summit.add(tuple(loc))
            allTrails.append(path)
            path=[]
        return(summit,allTrails)
    
    for mv in possibleMoves:
        # Store path to start (same for each possible move)
        origPath=copy.deepcopy(path)
        newPos =[loc[0]+mv[0],loc[1]+mv[1]]
        checkMoves(topoMap,newPos,path,summit,allTrails)
        # Need to reset path as multiple moves start at same location
        path=copy.deepcopy(origPath)

    # final ending is typically not at a summit, still want to return summit set and trail list
    return(summit,allTrails)


# Read input file 
#f=open('example.txt')
f=open('input.txt')
lines = f.read().splitlines();
f.close()
#

#Using numpy here for the convenience of "where"
topo=[]
for line in lines:
    row=[]
    for c in line:
       row.append(int(c))
    topo.append(row)
topoMap = np.array(topo)
startPt = np.where(topoMap==0)
x0=startPt[0]
y0=startPt[1]

partA = 0
partB = 0
for i in range(len(x0)):
    summit,allTrails = checkMoves(topoMap,[x0[i],y0[i]],[],set(),[])
    partA+=len(summit)
    partB+=len(allTrails)

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))



