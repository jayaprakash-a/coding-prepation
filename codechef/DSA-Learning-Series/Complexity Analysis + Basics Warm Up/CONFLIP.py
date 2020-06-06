T = int(input())
for _ in range(T):
	G = int(input())
	for _ in range(G):
		[I, N, Q]  = input().split()
		I, N, Q = int(I), int(N), int(Q)

		if N%2 == 0:
			print(N//2)
			continue
		else:
			if I == Q:
				print(N//2)
				continue
			else:
				print(N//2+1)
				continue
