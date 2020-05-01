class TrieNode:
	
	def __init__(self):

		self.children = [None]*26
		self.isWordEnd = False

class Trie:

	def __init__(self):

		self.root = TrieNode()

	def insert(self, word):

		temp = self.root

		for ch in word:
			if temp.children[ord(ch)-ord('a')] == None:
				temp.children[ord(ch)-ord('a')] = TrieNode()
			temp = temp.children[ord(ch)-ord('a')]


		temp.isWordEnd = True

	def search(self, word):
		temp = self.root
		isPresent = True
		for ch in word:
			if not temp:
				isPresent = False
				break
			temp = temp.children[ord(ch)-ord('a')]
		if isPresent and temp and temp.isWordEnd:
			return True

		return False

	def startsWith(self, word):

		temp = self.root
		isPresent = True
		for ch in word:
			if not temp:
				isPresent = False
				break
			temp = temp.children[ord(ch)-ord('a')]

		if isPresent and temp:
			return True

		return False



obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.search('app'))
print(obj.startsWith('app'))
obj.insert('app')
print(obj.search('app'))
