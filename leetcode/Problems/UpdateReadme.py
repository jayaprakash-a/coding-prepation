import glob
import os
import json

allFiles = glob.glob('*.py')

allFiles.remove('UpdateReadme.py')
allFiles.remove('UpdateTagList.py')
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

readmeFile = open('README.md', 'w')

fileHeaders = "# LEETCODE PROBLEMS\n\n| Problem number | Problem Name | Status | Difficulty |\n| -------------- | ------------ | ------ | ---------- |"
print(fileHeaders, file=readmeFile)
	# | 1              | Two Sum      | Easy   | Finished   |

for key in sorted(problemsDict.keys()):
	# print(problemsDict[key][0])
	question = problemsDict[key][0]
	questionName = ' '.join(question)
	print("| %d              | %s      | %s   | %s   |" % (key, questionName, 'Finished', problemsDict[key][1]), file=readmeFile)
# print("%s is %d years old." % (name, age))

readmeFile.close()

# dbFile = open('index.html', 'r')
# dbContent = dbFile.readlines()
# print(dbContent)
# problemDatabase = json.load(dbContent)

# print(problemDatabase['num_solved'])