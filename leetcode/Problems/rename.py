filePtr = open('solved.txt', 'r')
content = filePtr.readlines()
filePtr.close()

import os
fileDiff = {}
for fileDetails in content:
	fileDetails = fileDetails.strip().split(' ')
	fileDiff[fileDetails[0]] = fileDetails[-1]

for fileName in os.listdir('./'):
	if '-' in fileName and '.py' in fileName:
		fileNo = fileName.split('-')[0]
		newName = fileName.split('.py')[0] + '-' + fileDiff[fileNo] + '.py'
		os.rename(fileName, newName)