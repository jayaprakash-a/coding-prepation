def gcd(A, B):
	if A%B == 0:
		return B
	return gcd(B, A%B)
def getAns(N, A, B, K):
	lcm = (A*B)//gcd(max(A, B), min(A, B))
	return N//A + N//B - 2*(N//lcm) >= K
T = int(input())
for _ in range(T):
	[N, A, B, K] = [int(i) for i in input().strip().split()]
	if getAns(N, A, B, K):
		print('Win')
	else:
		print('Lose')