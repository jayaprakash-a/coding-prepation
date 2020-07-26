class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def helper(x):
            return list(map(order.index, x))
        return words == sorted(words, key=helper)