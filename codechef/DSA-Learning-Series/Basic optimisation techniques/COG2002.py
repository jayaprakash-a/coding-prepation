def getAns(arr):
	arr.append(arr[0])
	arr.append(arr[1])

	sumVal = arr[0]+arr[1]+arr[2]

	values = [sumVal]
	for i in range(3, len(arr)):
		sumVal -= arr[i-3]
		sumVal += arr[i]
		values.append(sumVal)

	return max(values)


T = int(input())
for _ in range(T):
	N = int(input())
	arr = [int(i) for i in input().strip().split()]
	print(getAns(arr))