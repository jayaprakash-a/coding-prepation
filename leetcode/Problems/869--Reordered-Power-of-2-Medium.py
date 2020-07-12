class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        actual = Counter(str(N))
        limit = int(''.join(sorted(str(N), reverse=True)))
        num = 1
        valid = []
        while num <= limit:
            number = Counter(str(num))
            if number == actual:
                return True
            num = num << 1
        return False