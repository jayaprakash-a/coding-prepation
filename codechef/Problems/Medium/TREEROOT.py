# https://www.codechef.com/problems/TREEROOT
# 2
# 1
# 4 0
# 6
# 1 5
# 2 0
# 3 0
# 4 0
# 5 5
# 6 5
def calc_root(vals, sums):
	N = len(vals)
	if N == 1:
		return vals[0]
	return sum(vals) - sum(sums)

def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		vals, sums = [], []
		for _ in range(N):
			[val, sumval] = list(map(int, input().split(' ')))
			vals.append(val)
			sums.append(sumval)
			answer = calc_root(vals, sums)
		print(answer)

main()