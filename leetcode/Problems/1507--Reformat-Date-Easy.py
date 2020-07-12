class Solution:
    def reformatDate(self, date: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        dateSplit = date.split(' ')
        answer = ''
        answer += (dateSplit[2] + '-')
        answer += str(month.index(dateSplit[1]) + 1).zfill(2) + '-'
        answer += dateSplit[0].replace('th', '').replace('st', '').replace('rd', '').replace('nd', '').zfill(2)
        
        return answer