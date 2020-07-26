def getAns(n):
	if n <= 6:
		return 1 <<(n-1)
	first, second, third, fourth, fifth, sixth = 1, 2, 4, 8, 16, 32
	prevSum = 63
	result = 0
	for i in range(7, n+1):
		temp = first
		first, second, third, fourth, fifth, sixth = second, third, fourth, fifth, sixth, prevSum
		prevSum = ((2*prevSum)%(10**9+7) - (temp)%(10**9+7))%(10**9+7)
	return sixth%(10**9+7)
def main():
	n = int(input())
	print(getAns(n))
main()

