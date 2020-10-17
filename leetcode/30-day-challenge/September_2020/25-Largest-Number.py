class Solution(object):
    def largestNumber(self, num):
        """
        :type nums: List[int]
        :rtype: str
        """
        # def largestNumber(self, num):
        comp=lambda a,b:1 if a+b>b+a else -1 if a+b<b+a else 0
        num=map(str,num)
        num.sort(cmp=comp,reverse=True)
        return str(int("".join(num)))