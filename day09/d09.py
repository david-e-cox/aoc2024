#!/usr/bin/python3

# defragment diskImage by block
def moveBlocks(diskImage):
    done = False
    lastBlock = len(diskImage)-1

    for i in range(0,len(diskImage)):
        if diskImage[i]==-1:
            diskImage[i]=diskImage[lastBlock]
            diskImage[lastBlock]=-1
            lastBlock-=1
            while diskImage[lastBlock]==-1:
                lastBlock-=1
            if (lastBlock-1)<=i:
                break

            
# defragment diskImage by file            
def moveFiles(diskImage,fileSize,spaceSize):
    for f in sorted(fileSize,reverse=True):
        for s in sorted(spaceSize):
            fileLen = fileSize[f]
            spaceAvail = spaceSize[s]
            if s > f:
                break
            if fileLen <= spaceAvail:
                del spaceSize[s]
                if (spaceAvail-fileLen) > 0:
                    spaceSize[s+fileLen] =(spaceAvail - fileLen)
                for i in range(0,fileLen):
                    diskImage[s+i] = diskImage[f+i]
                    diskImage[f+i] = -1
                break

# Count number of sequential entries in diskIamge that are equal
# used to find file length and length of empty space
def countSame(diskImage,ptr):
    done=False
    cnt=1
    if ptr+1>=len(diskImage):
        done=True
    while not done:
        if diskImage[ptr]!=diskImage[ptr+1]:
            done=True
        else:
            cnt+=1
            ptr+=1
        if ptr+1>=len(diskImage):
            done=True
    return(cnt)


# Create dictionaries with filesystem data, startpoint(key) and size(value)
def findSpace(diskImage):
    spaceSize=dict()
    fileSize=dict()
    
    blockPtr=0
    while blockPtr<len(diskImage):
        if diskImage[blockPtr]>=0:
            sz = countSame(diskImage,blockPtr)
            fileSize[blockPtr] = sz
            blockPtr+=sz
        else:  # Space
            spaceSize[blockPtr]= countSame(diskImage,blockPtr)
            blockPtr+=spaceSize[blockPtr]
    return([fileSize,spaceSize])



# Parse input to create expanded disk image
def mkDiskImage(diskCode):
    cnt=0
    diskImage=[]
    for i in range(0,len(diskCode)-1,2):
        for j in range(0,int(diskCode[i])):
            diskImage.append(cnt)
        for j in range(0,int(diskCode[i+1])):
            diskImage.append(-1)
        cnt+=1
    
    for i in range(0,int(diskCode[-1])):
        diskImage.append(cnt)
    return(diskImage)

# Util to show diskimage
def showImage(di):
    for val in di:
        if val <0:
            print('.',end="")
        else:
            print("{}".format(val),end="")
    print()

    
        
# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()

#Create diskImage with file ID's spaning size of block
diskImageA = mkDiskImage(lines[0])
moveBlocks(diskImageA)
cnt=0
partA=0
for fileId in diskImageA:
    if fileId>=0:
        partA += cnt*fileId
    cnt+=1


diskImageB=mkDiskImage(lines[0])
partB=0
cnt=0
[fileSize,spaceSize] = findSpace(diskImageB)
moveFiles(diskImageB,fileSize,spaceSize)
for fileId in diskImageB:
    if fileId>=0:
        partB += cnt*fileId
    cnt+=1

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


