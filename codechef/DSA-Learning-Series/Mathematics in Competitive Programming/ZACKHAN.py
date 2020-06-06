def gcd(A, B):
	if A%B == 0:
		return B
	return gcd(B, A%B)

T = int(input())
for _ in range(T):
	[A, B] = [int(i) for i in input().strip().split()]
	print(gcd(max(A, B), min(A, B)))