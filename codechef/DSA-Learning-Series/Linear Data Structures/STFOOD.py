# 2
# 3
# 4 6 8
# 2 6 6
# 1 4 3
# 1
# 7 7 4
T = int(input())
for _ in range(T):
	N = int(input())
	maxVal = 0
	for _ in range(N):
		[s, p, v] = list(map(int, input().split()))
		num = p//(s+1)
		if num*v > maxVal:
			maxVal = num*v
	print(maxVal)