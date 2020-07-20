def getAns(times):
    times = sorted(times, key=lambda x:(x[0]))
    timeVal, reward = 0, 0
    for time in times:
        timeVal += time[0]
        reward += (time[1]-timeVal)
    return reward
def main():
    n = int(input())
    times = []
    for _ in range(n):
        times.append(list(map(int, input().split())))
    print(getAns(times))
main()