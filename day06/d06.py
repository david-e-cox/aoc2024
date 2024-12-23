#!/usr/bin/python3
import re
from collections import defaultdict
import copy

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()

roomMap=[]
for row in lines:
    roomMap.append(list(row))
    
def guardWalk(roomMap,pos):
    stepCnt=0
    path=[]
    direction=[]
    done=False
    turn=dict()
    move=dict()
    history = defaultdict(set)
    inLoop = False

    # dictionary as operations for turn/move
    turn['^'] = '>'
    turn['>'] = 'v'
    turn['v'] = '<'
    turn['<'] = '^'

    move['^'] = (-1,0)
    move['>'] = (0,1)
    move['v'] = (1,0)
    move['<'] = (0,-1)

    # The guard, represented with his directional character
    g = roomMap[pos[0]][pos[1]]

    # A history keyed by positions in the map, with a list-value for directions the guard walked when at that position
    # This is key to finding the loops, if the guard re-encounters the same postion and direction he is entering a loop
    history[(pos[0],pos[1])].add(g)

    while not done:
        # new postion, if valid
        P = ( pos[0]+move[g][0],  pos[1]+move[g][1] )
        # If it's in the history, set loopFlag
        if (P in history.keys()) and (g in history[P]):
            inLoop=True

        # If its off the map, end run (guard has left the room)
        if P[0]<0 or P[0]>(len(roomMap)-1) or P[1]<0 or P[1]>(len(roomMap[0])-1) or inLoop:
            done=True
            return([stepCnt+1,inLoop,path])

        # Turn if next-step is a obstacle, else reposition
        if roomMap[P[0]][P[1]]=='#':
            g=turn[g]
            roomMap[pos[0]][pos[1]]=g
            # Apppend path/direction history
            history[(pos[0],pos[1])].add(g)
        else:
            roomMap[pos[0]][pos[1]]='X'
            if roomMap[P[0]][P[1]]=='.':
                stepCnt+=1
            roomMap[P[0]][P[1]]=g
            path.append(P)
            history[(P[0],P[1])].add(g)

            # Update position, keep walking
            pos=P

# Show roomMap evolution with X history, (debug)        
#       for row in roomMap:
#           print("     {}".format("".join(row)))
 



guard = None
cnt   = 0;
while not guard:
    guard = re.search(r">|<|\^|v","".join(roomMap[cnt]))
    cnt+=1;

guardPosition = [cnt-1, guard.start()]
cleanMap      = copy.deepcopy(roomMap)
obsLoc        = set()
walkCounter   = 0

partA,inLoop,path = guardWalk(roomMap,guardPosition)

# For PartB we have to put an obstruction along every point in the original path
# Run the walker and detect entry into a loop
for loc in path:
    walkCounter+=1
    if walkCounter%25==0:
        print("Searching: {}/{}".format(walkCounter,len(path)))

    # Don't put a obstacle at the guards original location, he'll see it
    if loc==(guardPosition[0],guardPosition[1]):
        continue

    # Place obstruction along each spot in original path
    roomMap=copy.deepcopy(cleanMap)
    roomMap[loc[0]][loc[1]]='#'

    # Run walker, check for loops
    stepCnt,inLoop,newPath = guardWalk(roomMap,guardPosition)
    if inLoop:
        obsLoc.add(loc)

#print("Obstructions: {}".format(obsLoc))
partB = len(obsLoc)

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


