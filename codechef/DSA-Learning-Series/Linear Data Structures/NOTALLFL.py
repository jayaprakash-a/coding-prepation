# 2
# 6 2
# 1 1 1 2 2 1

T = int(input())
for _ in range(T):
	[N, K] = list(map(int, input().split(' ')))
	flavArr = list(map(int, input().split(' ')))
	flavDict = {}
	maxDiff = 0
	for i in range(N):
		if flavArr[i] not in flavDict.keys():
			flavDict[flavArr[i]] = [-1, i]
		else:
			flavDict[flavArr[i]] += [i]
	if len(flavDict.keys()) != K:
		print(N)
		continue
	else:
		
		for i in flavDict.keys():
			for j in range(len(flavDict[i])):
				diff = 0
				if j != len(flavDict[i])-1:
					diff = flavDict[i][j+1] - flavDict[i][j]
				else:
					diff = N - flavDict[i][j]
				if diff > maxDiff:
					maxDiff = diff
	print(maxDiff-1)
