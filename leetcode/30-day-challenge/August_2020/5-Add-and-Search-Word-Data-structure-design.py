class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(None)
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
            if not ch in temp.children:
                temp.children[ch] = TrieNode()
            temp = temp.children[ch]
        temp.isWordEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(node, word):
            if not word:
                if node and node.isWordEnd:
                    self.result = True
                return
            if not node:
                return
            if word[0] == '.':
                for key in node.children:
                    dfs(node.children[key], word[1:])
            else:            
                if not word[0] in node.children:
                    return
                node = node.children[word[0]]
                dfs(node, word[1:])
        self.result = False
        temp = self.root
        dfs(temp, word)
        
        return self.result
    
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)