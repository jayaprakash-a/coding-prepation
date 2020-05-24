# https://www.codechef.com/problems/AND
def get_bit(num, index):
	return (num >> index) & 1
def get_sum_of_and(nums):
	max_num = max(nums)
	max_ind = len(bin(max_num)) - 2
	answer = 0
	for ind in range(max_ind):
		one_count = 0
		for num in nums:
			if get_bit(num, ind) == 1:
				one_count += 1
		answer += ((1<<ind) * ((one_count)*(one_count-1)//2))
	return answer

def main():
	N = int(input())
	nums = list(map(int, input().split(' ')))
	answer = get_sum_of_and(nums)
	print(answer)

main()