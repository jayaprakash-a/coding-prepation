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

    def search(self, word: str) -> str:
        """
        Returns if the word is in the trie.
        """
        # print('Search call')
        iterator = self.root
        rootWord = ''
        for ch in word:
            if iterator.isWordEnd:
                return rootWord
            rootWord += ch
            
            # print('search', ch, word)
            if iterator.charArr[ord(ch)-ord('a')] != None:
                iterator = iterator.charArr[ord(ch)-ord('a')]
                continue
            elif iterator == None or iterator.charArr[ord(ch)-ord('a')] == None:
                # print('Return False')
                return ''
            else:
                iterator = iterator.charArr[ord(ch)-ord('a')]
            
        if iterator.isWordEnd:
            # print('Case2')
            return rootWord
        
        return ''
        
        

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        myPrefixTrie = Trie()
        for word in dict:
            myPrefixTrie.insert(word)
        sentWords = sentence.split(' ')
        for i in range(len(sentWords)):
            root = myPrefixTrie.search(sentWords[i])
            if root != '':
                sentWords[i] = root
        return ' '.join(sentWords)