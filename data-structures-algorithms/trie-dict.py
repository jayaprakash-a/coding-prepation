class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
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
        temp = self.root
        isPresent = True
        for ch in word:
            if not temp:
                isPresent = False
                break
            if not ch in temp.children:
                return False
            else:
                temp = temp.children[ch]
        if isPresent and temp and temp.isWordEnd:
            return True

        return False
              

    def startsWith(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.root
        isPresent = True
        for ch in word:
            if not temp:
                isPresent = False
                break
            if not ch in temp.children:
                return False
            else:
                temp = temp.children[ch]
        if isPresent and temp:
            return True

        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)