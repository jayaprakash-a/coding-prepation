n = int(input())
values = ['']
for _ in range(n):
    operations = input().split()
    if operations[0] == '1':
        values.append(values[-1]+operations[1])
    elif operations[0] == '2':
        k = int(operations[1])
        values.append(values[-1][:-k])
    elif operations[0] == '3':
        k = int(operations[1])
        print(values[-1][(k-1)])
    else:
        values.pop()
        
        
    