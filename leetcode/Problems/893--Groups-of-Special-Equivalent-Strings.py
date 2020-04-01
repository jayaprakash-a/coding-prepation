class Solution:
    def sortParity(self, word):
        word1, word2 = '', ''
        
        for i in range(len(word)):
            if i%2 == 0:
                word1 += word[i]
            else:
                word2 += word[i]
                
        return str(sorted(word1)+sorted(word2))
  
    
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        
        overallSet = {}
        
        for word in A:
            
            wordSet = self.sortParity(word)
            # print(word, wordSet)
            if wordSet not in overallSet.keys():
                overallSet[wordSet] = 1
            else:
                overallSet[wordSet] += 1
                
                
        return len(overallSet.keys())
                
        