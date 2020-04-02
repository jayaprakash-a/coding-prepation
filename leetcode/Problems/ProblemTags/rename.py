filePtr = open('solved.txt', 'r')
content = filePtr.readlines()
filePtr.close()

import os
fileDiff = {}
for fileDetails in content:
	fileDetails = fileDetails.strip().split(' ')
	fileDiff[fileDetails[0]] = fileDetails[-1]

for fileName in os.listdir('./'):
	if '-' in fileName:
		fileNo = fileName.split('-')[0]
		newName = fileName + '-' + fileDiff[fileNo]
		os.rename(fileName, newName)