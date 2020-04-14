class TrieNode:
    def __init__(self):
        self.charArr = [None]*26
        self.isWordEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        iterator = self.root
        for ch in word:
            if iterator.charArr[ord(ch)-ord('a')] == None:
                newNode = TrieNode()
                iterator.charArr[ord(ch)-ord('a')] = newNode
                # iterator.isWordEnd = False
                iterator = iterator.charArr[ord(ch)-ord('a')]
            else:
                iterator = iterator.charArr[ord(ch)-ord('a')]
                
        iterator.isWordEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # print('Search call')
        iterator = self.root
        for ch in word:
            # print('search', ch, word)
            if iterator.charArr[ord(ch)-ord('a')] != None:
                iterator = iterator.charArr[ord(ch)-ord('a')]
                continue
            elif iterator == None or iterator.charArr[ord(ch)-ord('a')] == None:
                # print('Return False')
                return False
            else:
                iterator = iterator.charArr[ord(ch)-ord('a')]
        if iterator.isWordEnd:
            # print('Case2')
            return True
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        iterator = self.root
        for ch in prefix:
            if iterator.charArr[ord(ch)-ord('a')] != None:
                iterator = iterator.charArr[ord(ch)-ord('a')]
                continue
            elif  iterator == None or iterator.charArr[ord(ch)-ord('a')] == None:
                return False
            else:
                iterator = iterator.charArr[ord(ch)-ord('a')]
        # if iterator.isWordEnd:
        #     # print('Case2')
        #     return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)