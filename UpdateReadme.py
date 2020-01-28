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
	entrySplit = entry.split('--')
	problemsDict[int(entrySplit[0])] = entrySplit[1]

readmeFile = open('README.md', 'w')

fileHeaders = "# LEETCODE PROBLEMS\n\n| Problem number | Problem Name | Status | Difficulty |\n| -------------- | ------------ | ------ | ---------- |"
print(fileHeaders, file=readmeFile)
	# | 1              | Two Sum      | Easy   | Finished   |

for key in sorted(problemsDict.keys()):
	question = problemsDict[key].split('-')
	questionName = ' '.join(question)
	print("| %d              | %s      | %s   | %s   |" % (key, questionName, '----', 'Finished'), file=readmeFile)
# print("%s is %d years old." % (name, age))

readmeFile.close()

# dbFile = open('index.html', 'r')
# dbContent = dbFile.readlines()
# print(dbContent)
# problemDatabase = json.load(dbContent)

# print(problemDatabase['num_solved'])