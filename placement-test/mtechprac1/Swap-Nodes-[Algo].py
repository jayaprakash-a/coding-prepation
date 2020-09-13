import os
import sys
import collections
def swapNodes(indexes, queries):
    left = [0]
    right = [0]
    depths = {}
    depths[1] = 1
    for i, [l, r] in enumerate(indexes):
        depths[l] = depths[i+1] + 1
        depths[r] = depths[i+1] + 1
        left.append(l)
        right.append(r)
    answer = []
    def inorder(node):
        stack = []
        order = []
        while True:
            if node != -1:
                stack.append(node)
                node = left[node]
            elif stack:
                node = stack.pop()
                order.append(node)
                node = right[node]
            else:
                break
        print(order, stack)
        return order
    def swap(swapdepth):
        queue = collections.deque()
        queue.append(1)
        while queue:
            node = queue.popleft()
            level = depths[node]
            if left[node] != -1:
                queue.append(left[node])
            if right[node] != -1:
                queue.append(right[node])
            if level%swapdepth == 0:
                left[node], right[node] = right[node], left[node] 
        
    for q in queries:
        swap(q)
        answer.append(inorder(1))
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
