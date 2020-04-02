# def reverseVowels(self, s: str) -> str:
def reverseVowels(s: str) -> str:

	left, right = 0, len(s) - 1
	
	vowelSet = ['a', 'e', 'i', 'o', 'u']
	
	sList = list(s)
	while (left < right):
		
		while(s[left] not in vowelSet and left < len(s)):
			print('Debug::left', left)
			left += 1
		while(s[right] not in vowelSet and right >= 0):
			print('Debug::right', right)
			right -= 1
		print('Debug::Post 2 while loops')
		if left >= right:
			break
		sList[left], sList[right] = sList[right], sList[left]
		left += 1
		right -= 1
		
		
	return ''.join(sList)


print(reverseVowels('hello'))