class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        answer = []
        a1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        a2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        a3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        
        
        for word in words:
            newWord = word.lower()
            if (all([ch in a1 for ch in newWord])or all([ch in a2 for ch in newWord]) or all([ch in a3 for ch in newWord])):
                # print(newWord)
                answer.append(word)
        
        return answer
        