def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = a[1:]
    b = b[1:]
    if len(set(a).union(set(b))) == n:
        print('I become the guy.')
    else:
        print('Oh, my keyboard!')
main()