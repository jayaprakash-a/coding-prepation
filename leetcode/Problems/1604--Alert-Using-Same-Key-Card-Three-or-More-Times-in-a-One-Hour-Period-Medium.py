class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        timings = defaultdict(list)
        for i in range(len(keyName)):
            time = int(keyTime[i].split(':')[0])*60 + int(keyTime[i].split(':')[1])
            timings[keyName[i]].append(time)
        answer = []
        for key in sorted(timings):
            timings[key] = sorted(timings[key])
            for i in range(len(timings[key])-2):
                start = timings[key][i]
                count = 1
                for j in range(i+1, min(i+4, len(timings[key]))):
                    if timings[key][j]-start <= 60:
                        count += 1
                    else:
                        break
                if count >= 3:
                    answer.append(key)
                    break
        return answer
                        