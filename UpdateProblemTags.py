# files = ['hash-table.txt', 'linked-list.txt', 'maths.txt', 'two-pointers.txt', 'strings.txt']

for filename in files:
	file1 = open(filename, 'r')
	contents = file1.readlines()
	file1.close()
	file1 = open(filename, 'w')
	for i in range(len(contents)):
	    if i % 2 == 0:
	            print(contents[i], file=file1, end='')

	file1.close()