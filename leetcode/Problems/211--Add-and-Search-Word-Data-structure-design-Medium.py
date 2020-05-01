class TrieNode:
    
    def __init__(self):

        self.children = [None]*26
        self.isWordEnd = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        temp = self.root

        for ch in word:
            if temp.children[ord(ch)-ord('a')] == None:
                temp.children[ord(ch)-ord('a')] = TrieNode()
            temp = temp.children[ord(ch)-ord('a')]


        temp.isWordEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.result = False
        temp = self.root
        self.dfs(temp, word)
        
        return self.result
    
    def dfs(self, node, word):
        if not word:
            if node and node.isWordEnd:
                self.result = True
            return
        if not node:
            return
        if word[0] == '.':
            for i in range(26):
                self.dfs(node.children[i], word[1:])
        else:
            node = node.children[ord(word[0])-ord('a')]
            if not node:
                return
            self.dfs(node, word[1:])