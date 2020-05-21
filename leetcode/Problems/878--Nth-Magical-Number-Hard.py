class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        if A < B:
            A, B = B, A
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        def lcm(a, b):
            return (a*b)//gcd(a, b)
        modVal = 10**9 + 7
        lcm = lcm(A, B)
        vals = []
        for i in range(A, lcm, A):
            vals.append(i)
        for i in range(B, lcm, B):
            vals.append(i)
        vals.append(lcm)
        vals = sorted(vals)
        if N%len(vals) == 0:
            return (N//len(vals))*vals[-1] % modVal
        if N > len(vals):
            return ((N//len(vals))*vals[-1] + vals[N%len(vals)-1]) % modVal
        else:
            return vals[N%len(vals)-1] % modVal