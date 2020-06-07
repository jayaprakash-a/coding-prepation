def getAns(arr):
	n = len(arr)
	pre = [0]*n
	suf = [0]*n
	preSum, suffSum = 0, 0
	for i in range(n):
		preSum += arr[i]
		suffSum += arr[n-i-1]
		pre[i] = preSum
		suf[n-i-1] = suffSum
	# print(pre, suf)
	# suf = suf[::-1]
	answer, index = float('inf'), -1
	for i in range(n):
		# print('debug', i, pre[i]+suf[i], answer)
		if pre[i]+suf[i] < answer:

			answer = pre[i]+suf[i]
			index = i+1
	return index
T = int(input())
for _ in range(T):
	N = int(input())
	arr = [int(i) for i in input().strip().split()]
	print(getAns(arr))