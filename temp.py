k = 3
n = 20

firstWins = [False for _ in range(n)]

for i in range(k):
	firstWins[i] = True

for i in range(k, n):
	for j in range(i-1, i-k-1, -1):
		if not firstWins[j]:
			firstWins[i] = True
			break

print(firstWins)