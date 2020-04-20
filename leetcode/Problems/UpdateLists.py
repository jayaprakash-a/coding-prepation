import glob
import os
import json

def processPythonFiles():
	allFiles = glob.glob('*.py')

	allFiles.remove('UpdateLists.py')
	allFiles.remove('UpdateProblemTags.py')

	problemsDict = {}
	for entry in allFiles:
		# print(entry)
		entry = entry[:-3]
		if '-' in entry:
			entrySplit = entry.split('--')

			probName = entrySplit[1].split('-')[:-1]
			probDiff = entrySplit[1].split('-')[-1]
			problemsDict[int(entrySplit[0])] = [probName, probDiff]

	return problemsDict

def updateReadme(problemsDict):
	readmeFile = open('README.md', 'w')

	fileHeaders = "# LEETCODE PROBLEMS\n\n| S. no | Problem Number | Problem Name | Status | Difficulty |\n| -------------- | ------------ | ------ | ---------- | ---------- |"
	print(fileHeaders, file=readmeFile)
		# | 1              | Two Sum      | Easy   | Finished   |
	i = 1
	for key in sorted(problemsDict.keys()):
		# print(problemsDict[key][0])
		question = problemsDict[key][0]
		questionName = ' '.join(question)
		print("| %d              | %d              | %s      | %s   | %s   |" % (i,key, questionName, 'Finished', problemsDict[key][1]), file=readmeFile)
		i += 1
	readmeFile.close()

def processTagFiles():
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
	return tagDict

def updateTagList(problemsDict):
	tagFile = open('TaggedList.csv', 'w')

	fileHeaders = "Problem Number;Problem Name;Status;Difficulty;Tags"
	print(fileHeaders, file=tagFile)

	for key in sorted(problemsDict.keys()):
		question = problemsDict[key][0]
		questionName = ' '.join(question)
		print("%d;%s;%s;%s" % (key, questionName, 'Finished', problemsDict[key][1]), file=tagFile, end='')
		# print("%d,%s,Easy" % (key, questionName.replace(',', ';')), file=tagFile, end='')

		for tag in tagDict.keys():
			
			if key in tagDict[tag]:
				print(",%s" % (tag), file=tagFile, end='')
		print(file=tagFile)
			
	tagFile.close()

if __name__ == '__main__':
	problemsDict = processPythonFiles()
	updateReadme(problemsDict)
	tagDict = processTagFiles()
	updateTagList(problemsDict)
