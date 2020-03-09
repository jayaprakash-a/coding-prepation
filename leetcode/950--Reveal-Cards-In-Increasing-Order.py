# Refer to the following link

# https://leetcode.com/problems/reveal-cards-in-increasing-order/discuss/201574/C%2B%2B-with-picture-skip-over-empty-spaces

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        answer = [0]*len(deck)
        deck = sorted(deck)
        i, j = 1, 1
        answer[0] = deck[0]
        while(i < len(deck)):
            while(answer[j] != 0):
                j = (j + 1)%len(deck)
            j = (j + 1)%len(deck)
            while(answer[j] != 0):
                j = (j + 1)%len(deck)
            
            answer[j] = deck[i]
            i += 1
            
            
        
        return answer
        