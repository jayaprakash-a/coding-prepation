T = int(input())
for _ in range(T):
	exp = input()
	val, answer = 0, -1
	prevZero = 0
	for i in range(len(exp)):
		if exp[i] == '<':
			val += 1
		elif exp[i] == '>':
			val -= 1
		if val < 0:
			answer = i
			break			
		elif val == 0:
			prevZero = i
	if answer != -1:
		print(answer)
	else:
		print(prevZero+1)
