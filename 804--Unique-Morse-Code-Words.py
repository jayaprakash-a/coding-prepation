class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseMap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        answerSet = set()
        
        for word in words:
            morseRep = ''
            for ch in word:
                morseRep += morseMap[ord(ch)-ord('a')]
            answerSet.add(morseRep)
        
        return len(answerSet)
        