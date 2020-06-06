def bin_search(arr, value):
	if len(arr) == 0:
		return -1
	l, r = 0, len(arr)-1
	minVal, minInd = float('inf'), -1
	while l <= r:
		mid = (l+r)//2
		if arr[mid] > value:
			minVal, minInd = arr[mid], mid
			r = mid-1
		elif arr[mid] <= value:
			l = mid+1
	return minInd

def get_answer(radii):
	answer = []
	for entry in radii:
		index = bin_search(answer, entry)
		if index == -1:
			answer.append(entry)
		else:
			answer[index] = entry

	print(len(answer), end = ' ')
	for entry in answer:
		print(entry, end= ' ')
	print()



T = int(input())
for _ in range(T):
	N = int(input())
	radii = [int(i) for i in input().strip().split()]
	get_answer(radii)