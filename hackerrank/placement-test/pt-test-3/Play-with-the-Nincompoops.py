def getAns(edges):
    n = len(edges) + 1
    return n%2
        
def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        edges.append(list(map(int, input().split())))
    print(getAns(edges))

main()