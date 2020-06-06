def removeAlternate(n): 
	if n == 1: 
		return 1  
	if n % 2 == 0: 
		return 2 * removeAlternate(n // 2)
	else: 
		return 2 * removeAlternate((n-1) // 2)

def brute(n):
	arr = [i+1 for i in range(n)]
	fibArr = [0, 1]
	for _ in range(n-2):
		fibArr += [(fibArr[-1]+fibArr[-2])%10]
	
	count, diff = 0, 1
	# arr[0] = 0
	fibArr[0] = 0
	while count != n-1:
		start = diff - 1
		diff *= 2
		
		while count != n-1 and start < n:
			
			arr[start] = 0
			fibArr[start] = 0
			count += 1
			# print('debug', diff, arr, start, 'count', count)
			start += diff
			
			
	index = sum(arr)
	answer = sum(fibArr)
	return index, answer

def getAns(n):
	# brute_ans = brute(n)
	iter = removeAlternate(n)
	# print('answer', iter, pattern[iter%len(pattern)])
	# print(n, brute_ans[1]%10==pattern[(iter-1)%len(pattern)], brute_ans[1]%10, pattern[(iter-1)%len(pattern)], 'index', brute_ans[0], iter)
	return pattern[(iter-1)%len(pattern)]

pattern = [0,1,1,2,3,5,8,3,1,4,5,9,4,3,7,0,7,7,4,1,5,6,1,7,8,5,3,8,1,9,0,9,9,8,7,5,2,7,9,6,5,1,6,7,3,0,3,3,6,9,5,4,9,3,2,5,7,2,9,1]
T = int(input())
for _ in range(T):
	N = int(input())
	print(getAns(N))
# print(pattern)
# T = int(input())
# fibArr = [0, 1]
# for _ in range(T-2):
# 	fibArr += [(fibArr[-1]+fibArr[-2])%10]
# print(fibArr)
# for i in range(3, T):
# 	# N = int(input())
# 	getAns(i)
