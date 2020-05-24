# https://www.codechef.com/problems/TADELIVE
def comp(x):
	return x[0]
def get_answer(A, B, x, y):
	values = []
	for i in range(len(A)):
		values += [[abs(A[i]-B[i]), A[i], B[i]]]
	values = sorted(values, reverse=True, key=comp)
	answer = 0
	for i in range(len(values)):
		if values[i][1] > values[i][2]:
			if x > 0:
				answer += values[i][1]
				x -= 1
			else:
				answer += values[i][2]
				y -= 1
		else:
			if y > 0:
				answer += values[i][2]
				y -= 1
			else:
				answer += values[i][1]
				x -= 1
	return answer

def main():
	[N, x, y] = list(map(int, input().split()))
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	answer = get_answer(A, B, x, y)
	print(answer)

main()