# 3
# 3 10 15 5 10 100
# 12 15 18
# 3 10 15 5 10 100
# 5 5 10
# 4 40 80 30 30 100
# 100 100 100 100
import math
import heapq
T = int(input())
for _ in range(T):
	[N, A, B, X, Y, Z] = list(map(int, input().split(' ')))
	contribArr = list(map(int, input().split(' ')))
	maxSum = 2*sum(contribArr)
	for i in range(N):
		contribArr[i] *= -1
	heapq.heapify(contribArr)
	dayCount = math.ceil((Z-B)/Y)
	piedUsers = A+X*(dayCount-1)
	hooliUsers = B+Y*(dayCount-1)
	# print(piedUsers, hooliUsers)
	contrib = 0
	count  = 0
	diff = Z-piedUsers
	# maxSum = 2*sum(contribArr)
	if maxSum < diff:
		# print('c1')
		print('RIP')
		continue
	while(len(contribArr) > 0 and contrib < diff):
		# print(contribArr)
		c = -1*heapq.heappop(contribArr)
		contrib += (c)
		count += 1
		if (c)//2 > 0:
			heapq.heappush(contribArr, -1*((c)//2))
	# print(contrib)
	if contrib < diff:
		# print('c2')
		print("RIP")
	else:
		print(count)