class Solution:
	def checkSubarraySum(self, nums: List[int], k: int) -> bool:
		if k == 0:
			for i in range(len(nums) - 1):
				if nums[i] == -1*nums[i + 1]:
					return True
			return False
		sumVals = [0]
		sum, count = 0, 0
		for i in range(len(nums)):
			sum += nums[i]
			sumVals += [sum]
		for i in range(len(sumVals)):
			for j in range(i+2, len(sumVals)):
				if (sumVals[j]-sumVals[i])%k == 0:
					return True
		return False
		