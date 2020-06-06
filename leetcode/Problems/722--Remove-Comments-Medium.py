class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        isSingle, isMulti = False, False
        multiLine = ''
        answer, i = [], 0
        
        while i < len(source):
            # print(i, source[i], answer)
            if isMulti and '*/' in source[i]:
                source[i] = multiLine + source[i][source[i].find('*/')+2:]
                multiLine = ''
                isMulti = False
            elif isMulti:
                i += 1
            else:
                i1, i2 = source[i].find('//'), source[i].find('/*')
                if i1 < i2:
                    if '//' in source[i]:
                        source[i] = source[i][:source[i].find('//')]
                    elif '/*' in source[i]:
                        ind1 = source[i].find('/*') 
                        ind2 = source[i][ind1+2:].find('*/')
                        # print(source[i], '---', source[i][ind1+2:], ind1, ind2)
                        if ind2 == -1:
                            source[i] = source[i][:ind1]
                            if len(source[i]):
                                multiLine += source[i]
                                i += 1
                            isMulti = True
                        else:
                            source[i] = source[i][:ind1] + source[i][ind1+4+ind2:]
                            isMulti = False                    
                    else:
                        if len(source[i]):
                            answer.append(source[i])
                        i += 1
                else:                    
                    if '/*' in source[i]:
                        ind1 = source[i].find('/*') 
                        ind2 = source[i][ind1+2:].find('*/')
                        # print(source[i], '---', source[i][ind1+2:], ind1, ind2)
                        if ind2 == -1:
                            source[i] = source[i][:ind1]
                            if len(source[i]):
                                multiLine += source[i]
                                i += 1
                            isMulti = True
                        else:
                            source[i] = source[i][:ind1] + source[i][ind1+4+ind2:]
                            isMulti = False    
                    elif '//' in source[i]:
                        source[i] = source[i][:source[i].find('//')]
                    else:
                        if len(source[i]):
                            answer.append(source[i])
                        i += 1
        return answer