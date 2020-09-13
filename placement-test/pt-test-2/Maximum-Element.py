def main():
    n = int(input())
    nums = []
    max_vals = []
    for _ in range(n):
        # print(nums, max_vals)
        query = list(map(int, input().split()))
        if len(query) == 2:
            nums.append(query[1])
            if len(max_vals) == 0 or max_vals[-1] <= query[1]:
                max_vals.append(query[1])
            else:
                max_vals.append(max_vals[-1])
        elif query[0] == 2:
            nums.pop()
            max_vals.pop()
        else:
            print(max_vals[-1])
main()