# 2
# 3
# 101011
# 3
# 100001
T = int(input())
for _ in range(T):
	N = int(input())
	goals = input()
	a, b = 0, 0
	answer = -1
	for i in range(len(goals)):
		if i%2 == 0 and goals[i] == '1':
			a += 1
		elif i%2 == 1 and goals[i] == '1':
			b += 1
		arem = N - (i+2)//2
		brem = N - (i+1)//2
		# print(i, arem, brem)
		if a-b > brem:
			answer = i+1
			break
		elif b-a > arem:
			answer = i+1
			break
	if answer == -1:
		print(2*N)
	else:
		print(answer)


