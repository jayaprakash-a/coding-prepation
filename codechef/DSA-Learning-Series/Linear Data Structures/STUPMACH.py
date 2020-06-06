# 1
# 3
# 2 1 3
def compare(x):
	return x[0], -x[1]
T = int(input())
for _ in range(T):
	N = int(input())
	capacity = list(map(int, input().split()))
	capOrder = [(capacity[i], i+1) for i in range(N)]
	cap = sorted(capOrder, key=compare)

	base = cap[0][1]
	capBase = cap[0][0]
	answer = cap[0][0]*N
	for i in range(1, N):
		if cap[i][1] > base:
			continue
		else:
			answer += ((cap[i][0]-capBase)*cap[i][1])
			base = cap[i][1]
			capBase = cap[i][0]
			if base == 1:
				break
	print(answer)
