class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if a == a[::-1] or b == b[::-1]:
            return True
        def brute(x, y):
            for i in range(len(x)):
                newStr = x[:i]+y[i:]
                if newStr == newStr[::-1]:
                    print(len(newStr), len(x), i, newStr)
                    return True
                newStr = y[:i]+x[i:]
                if newStr == newStr[::-1]:
                    print(len(newStr), len(x), i, newStr)
                    return True
        def check(x, y):
            print(x, y)
            newStr = [x[0]]
            newStr += list(y[1:])
            valid = [False for _ in range(len(newStr))]
            invalid = len(valid)
            for i in range(len(valid)):
                if i == len(valid)//2:
                    valid[i] = True
                    invalid -= 1
                    continue
                if newStr[i] == newStr[-(i+1)]:
                    valid[i] = True
                    invalid -= 1
            if invalid == 0:
                return True
            print(invalid)
            for i in range(len(valid)):
                # print(i, invalid, valid[i])
                newStr[i] = x[i]
                if newStr[i] != newStr[-(i+1)]:
                    if valid[i]:
                        valid[i] = False
                        invalid += 1
                    if i != len(valid)// 2 and valid[-(i+1)]:
                        valid[-(i+1)] = False
                        invalid += 1                   
                    if invalid == 0:
                        return True
                else:
                    if not valid[i]:
                        valid[i] = True
                        invalid -= 1
                    if i != len(valid)// 2 and not valid[-(i+1)]:
                        valid[-(i+1)] = True
                        invalid -= 1 
                    if invalid == 0:
                        return True
                if i == 241:
                    # print(newStr)
                    print(valid)
                    indices = [i for i, x in enumerate(valid) if x == False]

                    print(indices)
                    print(newStr)
                    print(list(enumerate(newStr)))
            return False
            # print('Hola')
        
        # print(check(a, b), check(b, a))
        # print('------------')
        print('brute', brute(a, b))
        return check(a, b) or check(b, a)

s1 = "uagtjzlodgdtthompzxevstiwxbtvsqzlzjzvbtgnmiivhbsrjxdsiokffebntcgncikbkqayjypacmuxsqrqfxpwmeltfjqywtysxnerstaggnaecmfhzfxvpmwzbqhzfhqvjxiykaeydyfxugbzkfuufkzbguxfydyeakyixjvqhfzhqbzwmpvxfzhfmceanggatsrenxsytwyqjftlemwpxfqrqsxumcapyjyaqkbkicngogcyewxztrzkilyaxhayulhxbkmpnhminnfzfpmmxbrtanvzsgpkafutcgwpmes"
s2 = "jborhxanknlappxgpddtyzytzcwliqiwtbdcilnmdkdqtajsenxluawwxflxldywqaexxvbjsypvosjoigzvmbstiiyfackljqoffiqveakodvecjxezayrkiftuqbttkuktpxpbfhokazpuiprvecgghxvcophjqknedpjytlzxwylzyluskbvzxzprdwujtvgrgdseflquowapdgyeosrmbejcutcfhznlulusakdjmzspuctnbeffkoisdxjrsbhviimngtbvzjzlzqsvtbxwitsvexzpmohttdgdolzjtgau"
a = Solution()
print(a.checkPalindromeFormation(s1, s2))            