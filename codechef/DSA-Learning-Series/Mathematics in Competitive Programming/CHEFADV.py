def getAns(N, M, X, Y):
	if N%X == 0 and M%Y == 0:
		return True
	elif N%X == 1 and M%Y == 1:
		return True
	else:
		return False
T = int(input())
for _ in range(T):
	[N, M, X, Y] = [int(i) for i in input().strip().split()]
	if X == 1 or Y == 1:
		if X == Y == 1:
			print('Chefirnemo')
		elif X == 1:
			if M%Y == 0:
				print('Chefirnemo')
			elif M%Y == 1 and N-X >= 1:
				print('Chefirnemo')
			else:
				print('Pofik')
		else:
			if N%X == 0:
				print('Chefirnemo')
			elif N%X == 1 and M-Y >= 1:
				print('Chefirnemo')
			else:
				print('Pofik')
	else:
		if getAns(N-1, M-1, X, Y):
			print('Chefirnemo')
		else:
			print('Pofik')