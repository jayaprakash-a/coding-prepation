class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        # print('--------')
        arr_s = '_'.join(map(str, arr))
        for i in range(len(arr)-m+1):
            valid = arr[i:i+m] * k
            valid = '_'.join(map(str, valid))
            if valid in arr_s:
                return True
        return False