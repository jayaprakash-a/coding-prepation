def getAns(arr, K, P):
	comp = [0]*len(arr)
	ind = 0
	for i in range(1, len(arr)):
		if abs(arr[i][1]-arr[i-1][1]) <= K:
			comp[arr[i][0]] = ind
			comp[arr[i-1][0]] = ind
		else:
			ind += 1
			comp[arr[i][0]] = ind

	for _ in range(P):
		[x, y] = [int(i) for i in input().strip().split()]
		if comp[x-1] == comp[y-1]:
			print('Yes')
		else:
			print('No')
def comp(x):
	return x[1]
# N = int(input())
[N, K, P] = [int(i) for i in input().strip().split()]
arr = [int(i) for i in input().strip().split()]
modArr = sorted([[i, arr[i]] for i in range(N)], key=comp)
getAns(modArr, K, P)