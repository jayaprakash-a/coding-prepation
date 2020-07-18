import heapq
def getAns(n, k, sessions):
	difficulty = [0 for _ in range(len(sessions)-1)]
	for i in range(1, len(sessions)):
		difficulty[i-1] = (sessions[i-1]-sessions[i])
	heapq.heapify(difficulty)
	# print(difficulty)
	count = 0
	while count < k:
		diff1 = abs(heapq.heappop(difficulty))
		m = k - count + 1
		if len(difficulty) != 0:
			diff2 = abs(heapq.heappop(difficulty))
			m = min(k-count, diff1//diff2)+1
			if m > diff1 and diff2 == 1:
				return 1
			heapq.heappush(difficulty, -1*diff2)
		newDiff1 = diff1//m
		newDiff2 = diff1 - (m-1)*newDiff1
		for _ in range(m-1):
			heapq.heappush(difficulty, -1*newDiff1)
		heapq.heappush(difficulty, -1*newDiff2)
		# print(m, difficulty)
		count += (m-1)
	return abs(heapq.heappop(difficulty))

def main():
	t = int(input())
	for i in range(1, t+1):
		[n, k] = list(map(int, input().split()))
		sessions = list(map(int, input().split()))
		print('Case #%d: %d'%(i, getAns(n, k, sessions)))

main()