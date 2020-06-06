def merge(arr, temp, left, mid, right):
	inversion_count = 0
	l, r, tempInd = left, mid+1, left
	while l <= mid and r <= right:
		if arr[l] <= arr[r]: 
			temp[tempInd] = arr[l] 
			tempInd += 1
			l += 1
		else: 
			temp[tempInd] = arr[r] 
			inversion_count += (mid - l + 1) 
			tempInd += 1
			r += 1
	
	while l <= mid:
		temp[tempInd] = arr[l] 
		tempInd += 1
		l += 1

	while r <= right:
		temp[tempInd] = arr[r] 
		tempInd += 1
		r += 1

	for tempInd in range(left, right+1):
		arr[tempInd] = temp[tempInd]

	return inversion_count


def sortFunc(arr, temp, left, right):
	inversion_count = 0
	if left < right:
		mid = (left+right)//2
		inversion_count += sortFunc(arr, temp, left, mid)
		inversion_count += sortFunc(arr, temp, mid+1, right)
		inversion_count += merge(arr, temp, left, mid, right)
	return inversion_count

def mergeSort(arr): 
	n = len(arr)
	temp = [0]*n 
	return sortFunc(arr, temp, 0, n-1) 


N = int(input())
arr = [int(i) for i in input().strip().split()]
print(mergeSort(arr))