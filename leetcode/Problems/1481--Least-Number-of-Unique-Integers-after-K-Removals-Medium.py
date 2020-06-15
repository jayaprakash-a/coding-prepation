class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = []
        visited = {}
        for i in range(len(arr)):
            num = arr[i]
            if num in visited:
                counter[visited[num]][1] += 1
            else:
                counter.append([num, 1])
                visited[num] = len(counter)-1
        def comp(x):
            return x[1]
        nums = sorted(counter, key=comp)
        if k == 0:
            return len(nums)
        removed, index = 0, 0
        for i in range(len(nums)):
            removed += nums[i][1]
            if removed == k:
                index = i+1
                break
            elif removed > k:
                index = i
                break
        # print(index)
        return len(nums)-index