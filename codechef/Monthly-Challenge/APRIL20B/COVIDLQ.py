# 3
# 3
# 1 0 1

T = int(input())
for _ in range(T):
	N = int(input())
	nums = input().split(' ')
	prev = -1
	isValid = True
	for i in range(len(nums)):
		if nums[i] == '1':
			if prev == -1:
				prev = i q
			elif i-prev < 6:
				print('NO')
				isValid = False
				break
			prev = i

	if isValid:
		print('YES')
