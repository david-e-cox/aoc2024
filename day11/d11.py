#!/usr/bin/python3
from collections import defaultdict
def blink(s):
    cnt=0
    for i in range(0,len(s)):
        if s[cnt]=='0':
            s[cnt]='1'
        elif len(s[cnt])%2==0:
            midPt=int(len(s[cnt])/2)
            sold = s[cnt];
            s[cnt]=sold[:midPt]
            s.insert(cnt+1,str(int(sold[midPt:])))
            cnt+=1
        else:
            s[cnt]=str(2024*int(s[cnt]))
        cnt+=1
    return(s)


def blinkB(sDict):
    updateDict = defaultdict(int)
    # For all existing stones (may have multiple occurances)
    for s in sDict.keys():
        # apply blink to each stone
        newSet = blink([s])
        # create (or append) dict entry with the number of occurances of that stone in line
        # This "blinks" all the stones of the same value in parallel
        for snew in newSet:
            updateDict[snew] += sDict[s]

    return(updateDict)
            
        
# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()
partA = 0
partB = 0

stones=lines[0].split(' ')
for i in range(0,25):
    stones=blink(stones)
#    print("{}/{}".format(i+1,25))
partA = len(stones)


stones=lines[0].split(' ')
sDict=defaultdict(int)
for s in stones:
    sDict[s]+=1
for i in range(0,75):
    sDict = blinkB(sDict)
#    print("{}/{}".format(i+1,75))
partB=sum(sDict.values())

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


