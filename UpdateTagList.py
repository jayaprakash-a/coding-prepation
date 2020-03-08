import glob
import os
import json

allTagFiles = glob.glob('ProblemTags/*.txt')
tagDict = {}
for entry in allTagFiles:
	tempFile = open(entry, 'r')
	contents = tempFile.readlines()
	problems = []
	for line in contents:
		line = line.rstrip()
		problems.append(int(line))
	tagName = entry.split('.')[0]
	tagDict[tagName.split('/')[1]] = problems
	tempFile.close()

allFiles = glob.glob('*.py')

allFiles.remove('UpdateReadme.py')
allFiles.remove('UpdateTagList.py')
allFiles.remove('UpdateProblemTags.py')

problemsDict = {}
for entry in allFiles:
	entry = entry[:-3]
	entrySplit = entry.split('--')
	problemsDict[int(entrySplit[0])] = entrySplit[1]

tagFile = open('TaggedList.csv', 'w')

fileHeaders = "Problem number,Problem Name,Difficulty,Tags"
print(fileHeaders, file=tagFile)

# for key in sorted(problemsDict.keys()):
# 	question = problemsDict[key].split('-')
# 	questionName = ' '.join(question)
# 	print("| %d              | %s      | %s   | %s   |" % (key, questionName, '----', 'Finished'), file=tagFile)
# print("%s is %d years old." % (name, age))
for key in sorted(problemsDict.keys()):
	question = problemsDict[key].split('-')
	questionName = ' '.join(question)
	print("%d,%s,Easy" % (key, questionName.replace(',', ';')), file=tagFile, end='')
	for tag in tagDict.keys():
		
		if key in tagDict[tag]:
			print(",%s" % (tag), file=tagFile, end='')
	print(file=tagFile)
			


tagFile.close()