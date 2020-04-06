# 2
# 3
# 6 6 6
# 3
# 0 1 0

T = int(input())
for _ in range(T):
	N = int(input())
	nums = list(map(int, input().split(' ')))
	nums = sorted(nums, reverse=True)
	profit = 0
	for i in range(len(nums)):
		profit += max((nums[i]-i), 0)
	print(profit%(10**9+7))