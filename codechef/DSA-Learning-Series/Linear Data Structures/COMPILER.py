T = int(input())
for _ in range(T):
	exp = input()
	val = 0
	prevZero = -1
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
	print(prevZero+1)
