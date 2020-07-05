class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # return ''
        count = {}
        for ch in votes[0]:
            count[ch] = collections.Counter()
        self.n = len(votes[0])
        for vote in votes:
            for i in range(self.n):
                count[vote[i]][i] += 1
        def helper(x):
            val = list(count[x][i] for i in range(self.n)) + [-ord(x)]
            return tuple(val)
        return ''.join(sorted(votes[0], key=helper, reverse=True))