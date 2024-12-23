#!/usr/bin/python3
from collections import defaultdict
import itertools

def calcNodes(antennaLoc,citySizeRow,citySizeCol,withResonantHarmonics):
    antinodes=[]
    for pairs in itertools.combinations(antennaLoc,2):
        deltaX = pairs[1][0]-pairs[0][0]
        deltaY = pairs[1][1]-pairs[0][1]

        if withResonantHarmonics:
            # City is square row/col doesn't matter
            minExtent = -citySizeRow
            maxExtent = citySizeRow
        else:
            minExtent=0
            maxExtent=1

        # for partA only +1 is multiplier on deltas
        # for partB need a range of +/- integers on deltas
        # using citySize to set max range, logic tosses off map values
        for i in range(minExtent,maxExtent):
            anti = (pairs[0][0]-(i+1)*deltaX,pairs[0][1]-(i+1)*deltaY)
            if (anti[0]>=0 and anti[0]<citySizeRow and
                anti[1]>=0 and anti[1]<citySizeCol):
                antinodes.append(anti)

            anti = (pairs[1][0]+(i+1)*deltaX,pairs[1][1]+(i+1)*deltaY)
            if (anti[0]>=0 and anti[0]<citySizeRow and
                anti[1]>=0 and anti[1]<citySizeCol):
                antinodes.append(anti)
        
    return(antinodes)


# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()

# Create antenna database, using freq as key, list for the locations
antenna=defaultdict(list)
for i in range(0,len(lines)):
    for j in range(0,len(lines[i])):
        c=lines[i][j]
        if c != '.':
            antenna[c].append((i,j))

#Initialize            
partA = 0
partB = 0
uniqueAntinodesA=set()
uniqueAntinodesB=set()

#
for freq in antenna.keys():
    antinodes = calcNodes(antenna[freq],len(lines),len(lines[i]),False)
    for an in antinodes:
        uniqueAntinodesA.add(an)
partA=len(uniqueAntinodesA)

for freq in antenna.keys():
    antinodes = calcNodes(antenna[freq],len(lines),len(lines[i]),True)
    for an in antinodes:
        uniqueAntinodesB.add(an)
partB=len(uniqueAntinodesB)

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


