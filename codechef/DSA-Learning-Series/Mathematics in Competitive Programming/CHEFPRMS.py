def computeSemiPrime(N):
	# print('semi_primes')
	semi_primes = set()   
	for i in range(2, N+1):   
		count, num, j, primeCount = 0, i, 2, 0
		while count < 2 and j <= i and num != 1:  
			if num % j == 0:
				primeCount += 1
			while num % j == 0:  
				num //= j  
				count += 1

			j += 1
 
		if num > 1: 
			count += 1
		# print(i, count, primeCount)
		if count == 2 and primeCount == 2: 
			semi_primes.add(i)
	return semi_primes

def getAns(N):
	semi_primes = computeSemiPrime(N)
	# print(semi_primes)
	for num in semi_primes:
		if N - num in semi_primes:
			return 'YES'

	return 'NO'

T = int(input())
for _ in range(T):
	N = int(input())
	print(getAns(N))