def getAns(N):
	if N <= 1:
		return 0
	elif N <= 3:
		return 1
	answer = [0]*(N+1)
	answer[2] = 1
	answer[3] = 1

	for i in range(4, N+1):
		for j in [2, 3]:
			answer[i] += answer[i-j]
	return answer[-1]

T = int(input())
for _ in range(T):
	N = int(input())
	print(getAns(N))