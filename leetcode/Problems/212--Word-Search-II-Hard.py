class TrieNode:
    def __init__(self):
        self.data = {}
        self.endOfWord = False
        self.val = ""
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        current = self.root
        S = ""
        for char in word:
            S += char
            if char not in current.data:
                current.data[char] = TrieNode()
            current = current.data[char]
            current.val = S
        current.endOfWord = True
    def search(self,word):
        current = self.root
        for char in word:
            if char not in current.data:
                return False
            current = current.data[char]
        return (current.endOfWord == True)
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        
        def wordSearch(current,i,j):
            if trie.search(current.val):
                result.add(current.val)
            if i < 0 or j < 0 or i > (len(board) - 1) or j > (len(board[0]) - 1) or visited[i][j]:
                return 
            if board[i][j] not in current.data:
                return 
            visited[i][j] = True
            wordSearch(current.data[board[i][j]],i+1,j)
            wordSearch(current.data[board[i][j]],i,j+1)
            wordSearch(current.data[board[i][j]],i-1,j)
            wordSearch(current.data[board[i][j]],i,j-1)
            visited[i][j] = False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                wordSearch(trie.root,i,j)
        return list(result)