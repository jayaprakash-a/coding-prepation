import math
def getAns(N):
	start = math.floor(math.sqrt(N))
	answer = 0
	while start:
		prod = start*start
		if N-prod<=700 and N-prod>=0:
			answer += N-prod
		else:
			if N-prod>=0:
				answer += (700*start)
				break
		start -= 1
		
	return answer

T = int(input())
for _ in range(T):
	N = int(input())
	print(getAns(N))