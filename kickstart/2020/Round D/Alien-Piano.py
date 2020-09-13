def getAns(arr):
	newArr = [arr[0]]
	for i in range(1, len(arr)):
		if arr[i] != newArr[-1]:
			newArr.append(arr[i])
	answer, up, down = 0, 0
	for i in range(1, len(newArr)):
		if newArr[i] > newArr[i-1]:
			up += 1
			down = 0
		else:
			down += 1
			up = 0
		if up > 3 or down > 3:
			answer += 1
			up = down = 0
	
	return answer


def main():
	t = int(input())
	for i in range(1, t+1):
		n = int(input())
		arr = list(map(int, input().split()))
		print('Case #%d: %d'%(i, getAns(arr)))
main()