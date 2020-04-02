# files = ['binary-search.txt', 'divide-and-conquer.txt']
# files = ['ProblemTags/bit-manipulation.txt', 'ProblemTags/dynamic-programming.txt']
for filename in files:
	file1 = open('ProblemTags/'+filename, 'r')
	contents = file1.readlines()
	file1.close()
	file1 = open('ProblemTags/'+filename, 'w')
	for i in range(len(contents)):
	    if i % 3 == 0:
	        print(contents[i], file=file1, end='')

	file1.close()