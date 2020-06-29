class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod = [0]*k
        for num in arr:
            mod[num%k] += 1
        for i in range(1, k):
            # print()
            if mod[i] != mod[k-i]:
                return False
        return True and mod[0]%2 == 0