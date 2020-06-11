class Solution:
	def largestMultipleOfThree(self, digits: List[int]) -> str:
		def getAns(digits):
			counter = collections.Counter(digits)
			if counter[0] == len(digits) and len(digits) != 0:
				return '0'			
			answer = ''
			for num in range(9, -1, -1):
				answer += (str(num)*counter[num])
			return answer
		def getSolution(digits, p1, p2):
			count = 0
			for num in p1:
				if num in digits:
					digits.remove(num)
					return getAns(digits)
			for num in p2:
				if num in digits:
					digits.remove(num)
					count += 1
				if count == 2:
					return getAns(digits)
		
		sumVal = sum(digits)    
		if sumVal % 3 == 0:
			return getAns(digits)
		elif sumVal % 3 == 1:
			return getSolution(digits, [1, 4, 7], [2, 2, 5, 5, 8, 8])
		else:
			return getSolution(digits, [2, 5, 8], [1, 1, 4, 4, 7, 7])