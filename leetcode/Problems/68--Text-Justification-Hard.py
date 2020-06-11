class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer, index = [], 0
        while(index < len(words)):
            string = [words[index]]
            length = len(words[index])
            index += 1
            while(index < len(words) and length  + (len(words[index]) + 1) <= maxWidth):
                length += (len(words[index]) + 1)
                string += [words[index]]
                index += 1
            insert = ''
            if len(string) > 1:
                gap = (maxWidth - length)//(len(string)-1)
                extra = (maxWidth - length)%(len(string)-1)                
                for i in range(len(string)-1):
                    insert += string[i]
                    if extra:
                        insert += ' '*(gap+2)
                        extra -= 1                          
                    else:
                        insert += ' '*(gap+1)
            insert += string[-1]
            insert += (' '*maxWidth)
            answer.append(insert[:maxWidth])
        lastRow = answer[-1]
        lastString = ''
        for word in lastRow.split(' '):
            if len(word) > 0:
                lastString += word
                lastString += ' '
        lastString += (' '*maxWidth)
        answer[-1] = lastString[:maxWidth]
        return answer
            