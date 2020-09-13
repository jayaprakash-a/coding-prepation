def getAns(pac, food, matrix):
    # print(matrix)
    answer = []
    
    stack = [pac]
    dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    matrix[pac[0]][pac[1]] = '%'
    path = {tuple(pac):((-1, -1), 0)}
    while stack:
        node = stack.pop()
        answer.append(node)
        if node == food:
            break
            
        for entry in dirs:
            newNode = [node[0]+entry[0], node[1]+entry[1]]
            if matrix[newNode[0]][newNode[1]] == '%':
                continue
            else:
                matrix[newNode[0]][newNode[1]] = '%'
                stack.append(newNode)
                path[tuple(newNode)] = (tuple(node), path[tuple(node)][1]+1)
    print(len(answer))
    for entry in answer:
        print(entry[0], entry[1])
    print(path[tuple(food)][1])
    
    node = food
    result = []
    while node != (-1, -1):
        result.append(node)
        
        node = path[tuple(node)][0]
    for entry in result[::-1]:
        print(entry[0], entry[1])
        
def main():
    pac = list(map(int, input().split()))
    food = list(map(int, input().split()))
    [n, m] = list(map(int, input().split()))
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    getAns(pac, food, matrix)

main()