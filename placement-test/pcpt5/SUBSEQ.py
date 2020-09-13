def getAns(nums):
	if len(nums) == 0:
		return 0
	up, down = 1, 1
	for i in range(1, len(nums)):
		if nums[i] > nums[i-1]:
			up = down+1
		elif nums[i] < nums[i-1]:
			down = up+1
	return max(up, down)
	
def main():
	n = int(input().strip())
	arr = list(map(int, input().strip().split()))
	print(getAns(arr))
main()