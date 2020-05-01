class Solution:
    def compare(self, x):
        return -x[1], x[0]
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        w = collections.Counter(words).items()
        w =  sorted(w, key=self.compare)
        return [x[0] for x in w][:k]