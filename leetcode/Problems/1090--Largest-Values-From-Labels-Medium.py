class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        order = sorted(zip(values, labels), reverse=True)
        count = collections.Counter()
        answer, i = 0, 0
        while num_wanted > 0 and i < len(values):
            val, label = order[i]
            i += 1
            if count[label] < use_limit:
                count[label] += 1
                num_wanted -= 1
                answer += val
        return answer