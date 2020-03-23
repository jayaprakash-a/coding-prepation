
def main():
	T = int(input())

	for i in range(T):

		N, budget = [int(x) for x in input().split()]
		cost = [int(x) for x in input().split()]
		cost = sorted(cost)
		sumVal = 0
		answer = 0
		for c in cost:
		    sumVal += c
		    if sumVal > budget:
		        break
		    answer += 1
		print(('Case #%d: %d')%(i+1,answer))


if __name__ == '__main__':
	main()
