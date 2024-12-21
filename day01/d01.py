#!/usr/bin/python3
import numpy as np

# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()

data = np.array([ [int(x) for x in line.split()] for line in lines])
partA = np.sum(np.abs(np.diff(np.sort(data,axis=0),axis=1)))

partB = 0
for v in data[:,0]:
    partB += v*np.sum(data[:,1]-v==0)

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


