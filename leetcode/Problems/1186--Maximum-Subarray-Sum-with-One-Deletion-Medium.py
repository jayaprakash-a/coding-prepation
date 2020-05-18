class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        max_one_del = arr[0]
        max_no_del = arr[0]
        overall_max = arr[0]
        
        for num in arr[1:]:
            max_one_del = max(max_one_del + num, max_no_del, num)
            max_no_del = max(max_no_del + num, num)
            overall_max = max(overall_max, max_one_del, max_no_del)
        return overall_max