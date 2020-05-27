# https://www.codechef.com/problems/CHRL1
def get_answer(k, cost, weight):
	# print('DEBUG', cost)
	# print('DEBUG', weight)
	dp = [[0 for _ in range(len(weight))] for _ in range(k)]
	for i in range(k):
		for j in range(len(weight)):
			if cost[j] <= i:
				# print('DEBUG', i, j, cost[j], i)
				dp[i][j] = max(dp[i-cost[j]][j-1] + weight[j], dp[i][j-1])
	# print(dp)
	return dp[-1][-1]

def main():
	T = int(input())
	for _ in range(T):
		[n, k] = map(int, input().split())
		cost, weight = [], []
		for _ in range(n):
			[c, w] = map(int, input().split())
			cost.append(c)
			weight.append(w)
		answer = get_answer(k, cost, weight)
		print(answer)

main()