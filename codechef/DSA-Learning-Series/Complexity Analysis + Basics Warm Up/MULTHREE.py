def get_answer(k, d0, d1):
	sumVal = d0 + d1
	for _ in range(k-2):
		d0, d1 = d1, (d0+d1)%10
		sumVal += d1
	return sumVal % 3 == 0
T = int(input())
for _ in range(T):
	[K, d0, d1] = map(int, input().split(' '))
	if get_answer(K, d0, d1):
		print('YES')
	else:
		print("NO")
