class Solution:
	def isNumber(self, s: str) -> bool:
		dfa = [
			{' ': 0, 'sign': 1, '.': 2, 'digit': 3},
			{'.': 2, 'digit': 3},
			{'digit': 4},
			{'digit': 3, '.': 5, 'e': 6, ' ': 9},
			{'digit': 4, 'e': 6, ' ': 9},
			{'digit': 5, 'e': 6, ' ': 9},
			{'sign': 7, 'digit': 8},
			{'digit': 8},
			{'digit': 8, ' ': 9},
			{' ': 9}            
		]
		state = 0
		for ch in s:
			if ch.isdigit():
				ch = 'digit'
			elif ch in '+-':
				ch = 'sign'
			if ch not in dfa[state].keys():
				# print(ch, s, state)
				return False
			state = dfa[state][ch]
		
		if state == 3 or state == 4 or state == 5 or state == 8 or state == 9:
			return True
		return False