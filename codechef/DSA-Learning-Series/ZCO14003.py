N = int(input())
budgets = []
for _ in range(N):
	num = int(input())
	budgets.append(num)
budgets = sorted(budgets)

budgets = [budgets[i]*(N-i) for i in range(N)]
print(max(budgets))