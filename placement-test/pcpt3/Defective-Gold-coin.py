import math
def main():
    n = int(input())
    for _ in range(n):
        num = int(input())
        answer = math.ceil(math.log(num, 3))
        print(int(answer))
main()