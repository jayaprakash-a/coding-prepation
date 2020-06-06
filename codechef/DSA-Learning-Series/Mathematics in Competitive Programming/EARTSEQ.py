def sieveOfEratosthenes(n): 

	prime = [True for i in range(n + 1)] 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True): 			  
			for i in range(p * 2, n + 1, p): 
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	primes = []
	for p in range(n + 1): 
		if prime[p]: 
			primes.append(p)
	return primes

def getAns(n):
	answer = []
	for i in range(n-1):
		# print(primes[i]*primes[i+1], end=' ')
		val = primes[i]*primes[i+1]
		if val > 1e9:
			print('-1')
			return
		answer.append(val)
	val = primes[n-1]*primes[0]
	if val > 1e9:
		print('-1')
		return
	answer.append(val)
	for num in answer:
		print(num, end = ' ')
	print()

primes = sieveOfEratosthenes(611954)
# print(len(primes))
T = int(input())
for _ in range(T):
	N = int(input())
	getAns(N)