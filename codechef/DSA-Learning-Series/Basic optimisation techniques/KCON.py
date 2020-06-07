def maxSubArray(nums):
	maxInc = nums[0]
	maxOverall = nums[0]
	for i in range(1, len(nums)):
		maxInc = max(nums[i], nums[i]+maxInc)
		maxOverall = max(maxOverall, maxInc)
	return maxOverall

def getAns(arr, k):
	if len(arr) == 0:
		return 0
	if len(arr) == 1 and arr[0] >= 0:
		return (k*arr[0])
	elif len(arr) == 0 and arr[0] < 0:
		return 0
	if sum(arr) < 0 or k == 2:
		return maxSubArray(arr+arr)
	elif k == 1:
		return maxSubArray(arr)
	
	maxPre = float('-inf')
	sumVal = 0
	for num in arr:
		sumVal += num
		maxPre = max(maxPre, sumVal)
	
	maxSuff = float('-inf')
	sumVal = 0        
	for num in arr[::-1]:
		sumVal += num
		maxSuff = max(maxSuff, sumVal)
	return (maxSuff+(k-2)*sum(arr)+maxPre)

T = int(input())
for _ in range(T):
	# N = int(input())
	[N, K] = [int(i) for i in input().strip().split()]
	arr = [int(i) for i in input().strip().split()]
	print(getAns(arr, K))