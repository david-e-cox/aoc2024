#!/usr/bin/python3
import numpy as np

# Read input file
#f=open('example.txt')
f=open('input.txt');
lines = f.read().splitlines();
f.close()

buttonA=[]
buttonB=[]
prize=[]
for i in range(0,len(lines),4):
    tmp=lines[i].split(',')
    Ax =  int(tmp[0].split('+')[1])
    Ay =  int(tmp[1].split('+')[1])
    buttonA.append((Ax,Ay))

    tmp=lines[i+1].split(',')
    Bx =  int(tmp[0].split('+')[1])
    By =  int(tmp[1].split('+')[1])
    buttonB.append((Bx,By))

    tmp=lines[i+2].split(',')
    Px =  int(tmp[0].split('=')[1])
    Py =  int(tmp[1].split('=')[1])
    prize.append((Px,Py))

partA = 0
partB = 0
possiblePrizesA=0

# Linear algebra problem, no optimization, only one soluton exists
# Only questionable tactic is moving to floating point for matrix inverse
# I'm using "round" to check interger-ness of solutions
# This gets fragile in partB
for i in range(0,len(buttonA)):    
    M   = np.transpose(np.array([buttonA[i],buttonB[i]]))
    sol = np.linalg.inv(M)@np.array(prize[i])

    if sol[0]>=0 and sol[0]<=100 and sol[1]>=0 and sol[1]<=100:
        possiblePrizesA+=1
        # horseshoes, hand-grenades and claw prize
        if all(np.round(sol,0) == np.round(sol,6)):
            partA += int( np.round(sol[0])*3 + np.round(sol[1]) )

for i in range(0,len(buttonA)):    
    M   = np.transpose(np.array([buttonA[i],buttonB[i]]))
    sol = np.linalg.inv(M)@np.array((prize[i][0]+10000000000000, prize[i][1]+10000000000000))
    # horseshoes, hand-grenades and claw prize
    if all(np.round(sol,0) == np.round(sol,3)):
        partB += int( np.round(sol[0])*3 + np.round(sol[1]) )

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))

