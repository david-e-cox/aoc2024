#!/usr/bin/python3
import numpy as np

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()

partA = 0
partB = 0
for line in lines:
    report = np.array([int(x) for x in line.split()])
    # Safe if the report is both monotonic (increasing or decreasing) and slowly changing
    monotonic = np.all(np.diff(report)>0) | np.all(np.diff(report)<0)
    slow = np.all(np.abs(np.diff(report))<=3)
    safe = monotonic & slow
    if safe:
        partA+=1
        partB+=1

    # If not safe, see if damper will allow (remove one level and retest)
    if not safe:
        for level in range(0,np.size(report)):
            dampReport = np.delete(report,level)
            monotonic = np.all(np.diff(dampReport)>0) | np.all(np.diff(dampReport)<0)
            slow = np.all(np.abs(np.diff(dampReport))<=3)
            dampSafe = monotonic & slow
            # Add these reports to the ones safe by partA standards
            if dampSafe:
                partB+=1
                break
            
                           
print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


