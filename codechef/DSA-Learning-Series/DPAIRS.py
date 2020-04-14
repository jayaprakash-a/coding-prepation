# 3 2
# 10 1 100
# 4 3

[N, M] = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

amax = max(A)
bmin = min(B)
aInd = A.index(amax)
bInd = B.index(bmin)

for i in range(N):
	print(i, bInd)
for i in range(M):
	if i!= bInd:
		print(aInd, i)