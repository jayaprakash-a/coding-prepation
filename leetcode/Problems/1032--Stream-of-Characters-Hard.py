class TrieNode: 
    def __init__(self):
        self.children = defaultdict()
        self.isWordEnd = False    

class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.maxLen = 0
        for word in words:
            self.maxLen = max(self.maxLen ,len(word))
            self.insert(word[::-1])
        self.q = ''
    
    def insert(self, word):
        temp = self.root
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = TrieNode()
            temp = temp.children[ch]
        temp.isWordEnd = True
    
  
    def query(self, letter: str) -> bool:
        
        self.q = (letter + self.q)[:self.maxLen]
        temp = self.root
        for ch in self.q:
            if not temp:
                return False
            if ch not in temp.children:
                return False
            if temp.children[ch] and temp.children[ch].isWordEnd:
                return True
            temp = temp.children[ch]