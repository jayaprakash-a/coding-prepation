# https://discuss.codechef.com/t/chefsqrs-editorial/59476
import math
def checkSquare(num):
	return math.ceil(math.sqrt(num))**2 == math.floor(math.sqrt(num))**2 == num
def getAns(N):
	value = float('inf')
	for i in range(1, math.ceil(math.sqrt(N))):
		b = (N//i - i)//2
		if checkSquare(N+b**2):
			value = min(value, b**2)
	if value == float('inf'):
		return -1
	return value
T = int(input())
for _ in range(T):
	N = int(input())
	print(getAns(N))