# 20
# 1 2 1 1 2 2 1 2 1 1 2 1 2 2 1 1 2 1 2 2
N = int(input())
brackets = input().split(' ')
brac = []
val = 0
for ch in brackets:
	if ch == '1':
		val += 1
	else:
		val -= 1

	brac.append(val)

maxDepth = max(brac)
maxInd = 0
for i in range(N):
	if brac[i] == maxDepth:
		maxInd = i
		break
prevInd = -1
maxLen = 0
# print(brac)
prevZero = -1
for i in range(N):
	if brac[i] == 0:

		# print(i, prevZero, maxLen)
		if i-prevZero>maxLen:
			maxLen = i-prevZero
			if i!= N-1:
				prevInd = prevZero
		prevZero = i
print(maxDepth, maxInd+1, maxLen, prevInd+2)
