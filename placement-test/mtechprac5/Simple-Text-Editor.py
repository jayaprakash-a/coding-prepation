def main():
    
    n = int(input().strip())
    answer = ['' for _ in range(n)]
    count = 1
    for _ in range(n):
        # print(answer[:count])
        query = list(map(str, input().strip().split()))
        if query[0] == '1':
            answer[count] = answer[count-1] + query[1]
            count += 1
        elif query[0] == '2':
            answer[count] = answer[count-1][:-int(query[1])]
            count += 1
        elif query[0] == '3':
            print(answer[count-1][int(query[1])-1])
        else:
            count -= 1
main()