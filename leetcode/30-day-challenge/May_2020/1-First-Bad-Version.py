# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        l, r = 1, n
        bad = n
        while l < r:
            mid = l + (r-l)//2
            midRes = isBadVersion(mid)
            if midRes:
                bad = mid
                r = mid
            else:
                l = mid+1
        
        return bad
                
            