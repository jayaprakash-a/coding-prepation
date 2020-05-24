# https://www.codechef.com/problems/MARBLES
def comp_val(n, k):
	answer = 1
	fact = 1
	for i in range(k):
		answer *= (n-i)
		fact *= (i+1)
	return answer//fact

def main():
	T = int(input())
	for _ in range(T):
		[n, k] = list(map(int, input().split(' ')))
		answer = comp_val(n-1, min(k-1, n-k))
		print(answer)

main()