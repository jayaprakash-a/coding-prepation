T = int(input())

for _ in range(T):
	num = int(input())
	five = 5
	count = 0
	while(num//five != 0):
		count += (num//five)
		five *= 5
	print(count)
