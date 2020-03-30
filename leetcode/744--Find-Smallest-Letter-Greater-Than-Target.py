class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letterSorted = sorted(letters)
        for ch in letterSorted:
            if ch > target:
                return ch
        return letterSorted[0]