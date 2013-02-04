# make shingles
import os
import pickle
#import collections


currentfilePath = os.path.realpath(__file__)
dirPath = currentfilePath.split("/")
dirPath[-1] = "test/"
dirPath = "/".join(dirPath)

filePathList = []
for x in range(0,100):
  if x<10:
    x = "0" + str(x)
  else:
    x = str(x)
  filePath = dirPath + "file" + x + ".txt" 
  filePathList.append(filePath)

#Shingle - ShingleID mapping  
shingleDict = {}

#Doc - ShingleID mapping
docShingleDict = {}
  
count = 0
for file in filePathList:
  print file
  f = open(file,"r")
  words = f.read().split(" ")
  
  #print len(words)
  temp = set()
  for index in range(0,len(words)-2):
    shingle = words[index] + " " + words[index+1] + " " + words[index+2]
    if shingle not in shingleDict.iterkeys():
      shingleDict[shingle] = count
      count = count + 1
      
    temp.add(shingleDict[shingle])
  
  docShingleDict[file.split("/")[-1].split(".")[0]] = temp
  
print len(shingleDict)
output = open("docShingleDict.pkl", 'wb')
pickle.dump(docShingleDict, output)
output.close()


