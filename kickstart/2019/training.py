T = int(input())

for i in range(T):

	N, P = [int(x) for x in input().split()]
	arr = [int(x) for x in input().split()]

	arr = sorted(arr)
	arr = [x - arr[0] for x in arr]

	sumArr = [0]*(N+1)
	sumArr[0] = 0
	for j in range(N):
		sumArr[j+1] = sumArr[j]+arr[j]
	# print(sumArr, arr)
	minVal = sumArr[-1]*P
	for j in range(P, N+1):
		# print(j, arr[j-1], sumArr[j], sumArr[j-P])
		if (P*arr[j-1]) - (sumArr[j]-sumArr[j-P]) < minVal:
			minVal = P*arr[j-1] - (sumArr[j]-sumArr[j-P])

	print(minVal)
