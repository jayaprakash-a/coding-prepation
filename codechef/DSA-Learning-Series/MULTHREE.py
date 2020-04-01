T = int(input())
for _ in range(T):
	[K, d0, d1] = input().split(' ')
	if (int(d0)+int(d1))%3 == 0:
		print('YES')
	else:
		print("NO")
