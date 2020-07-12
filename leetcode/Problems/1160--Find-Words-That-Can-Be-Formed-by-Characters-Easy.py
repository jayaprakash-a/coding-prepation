class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars, count = Counter(chars), 0
        for word in words:
            w = Counter(word)
            if chars&w == w:
                count += len(word)
        return count