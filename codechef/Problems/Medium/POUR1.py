# https://www.codechef.com/problems/POUR1
def gcd_two(a, b):
	# print('gcd_two', a, b)
	if a < b:
		a, b = b, a
	if a%b == 0:
		return b
	return gcd_two(b, a%b)

def gcd_three(a, b, c):
	return gcd_two(gcd_two(a, b), c)

def get_answer(a, b, c):
	# print('start', a, b)
	hcf = gcd_three(a, b, c)
	# print('hcf', hcf)
	a, b, c = a//hcf, b//hcf, c//hcf
	if a == 1:
		return c, 0
	elif b == 1:
		return  0, c
	else:
		x, y = get_answer(b, a%b, c)
		return y, x-(a//b)*y 

	# print('end', x, y)
	# return x, y

def main():
	T = int(input())
	for _ in range(T):
		a, b, c = int(input()), int(input()), int(input())
		if c > a and c > b:
			print(-1)
			continue
		x, y = get_answer(max(a, b), min(a, b), c)
		print(x, y)
		answer = 2*(abs(x) + abs(y))
		print(answer)

main()