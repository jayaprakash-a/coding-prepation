class Solution:
    def numberToWords(self, num: int) -> str:
        numMap = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
                 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
                 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
                 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
                 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
                 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        
        def thirdPlace(num):
            if num == 0:
                return []
            else:
                return [numMap[num], 'Hundred']
        def secondPlace(num):
            if num == 0:
                return []
            elif num <= 20:
                return [numMap[num]]
            else:
                if num %10 != 0:
                    return [numMap[(num//10) * 10], numMap[num%10]]
                else:
                    return [numMap[(num//10) * 10]]
        def combine(num):
            return thirdPlace(num//100) + secondPlace(num%100)
        
        if num == 0:
            return 'Zero'
        
        answer = []
        places = [1000000000, 1000000, 1000, 1]
        placeMap = {0: 'Billion', 1: 'Million', 2: 'Thousand', 3: ''}
        for i in range(len(places)):
            if num // places[i] == 0:
                continue
            else:
                answer += combine(num // places[i]) 
                answer += [placeMap[i]]
                num = num % places[i]
        # print(answer)
        return ' '.join(answer).strip()