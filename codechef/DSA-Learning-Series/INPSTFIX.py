T = int(input())
precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
for _ in range(T):
	N = int(input())
	exp = input().strip()
	ansStack = []
	ansExp = ''
	for ch in exp:
		if ch == '(':
			ansStack.append(ch)
		elif ch.isalpha():
			ansExp += ch
		elif ch == ')':
			while(ansStack[-1] != '('):
				ansExp += ansStack.pop()
			ansStack.pop()
		else:
			if len(ansStack) == 0:
				ansStack.append(ch)
			else:
				if ansStack[-1] == '(':
					ansStack.append(ch)
					continue
				while(len(ansStack) > 0 and ansStack[-1] in precedence.keys() and precedence[ch] <= precedence[ansStack[-1]]):
					ansExp += ansStack.pop()
				ansStack.append(ch)
	while (len(ansStack) > 0):
		ansExp += ansStack.pop()
	print(ansExp)



