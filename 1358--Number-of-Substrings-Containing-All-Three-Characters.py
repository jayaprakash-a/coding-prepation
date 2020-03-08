class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        a, b, c, length = [], [], [], len(s)
        for i in range(length):
            if s[i] == 'a':
                a.append(i)
            if s[i] == 'b':
                b.append(i)
            if s[i] == 'c':
                c.append(i)
                
        ai, bi, ci = 0, 0, 0
        # try:
        while(ai < len(a) and bi < len(b) and ci < len(c)):
            # print(a[ai], b[bi], c[ci])
            minVal = min(a[ai], b[bi], c[ci])
            maxVal = max(a[ai], b[bi], c[ci])
            count += (length - maxVal)
            if a[ai] < b[bi] and a[ai] < c[ci]:
                ai += 1
                # while(b[bi] < a[ai]):
                #     bi += 1
                # while(c[ci] < a[ai]):
                #     ci += 1
                # print('ai', bi, ci)
            elif b[bi] < a[ai] and b[bi] < c[ci]:
                bi += 1
                # while(a[ai] < b[bi]):
                #     ai += 1
                # while(c[ci] < b[bi]):
                #     ci += 1
                # print('bi', ai, ci)

            elif c[ci] < b[bi] and c[ci] < a[ai]:
                ci += 1
                # while(b[bi] < c[ci]):
                #     bi += 1
                # while(a[ai] < c[ci]):
                #     ai += 1
                # print('ci', ai, bi)
        # except:
            # pass
            
            # while()
            
                
                
            
        return count
            
        