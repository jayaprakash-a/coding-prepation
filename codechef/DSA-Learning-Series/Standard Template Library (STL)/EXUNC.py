# 5 5
# 2 2 7 14 14
# 1 1 3
# 1 2 6
# 2 2
# 2 4
# 2 5


[N, M] = list(map(int, input().split()))
A = list(map(int, input().split()))


S = set()
S.add(0)
for i in range(1, len(A)):
	if A[i]%A[i-1] != 0:
		S.add(i)

j = 0

while(j < M):
	task = list(map(int, input().split()))
	if task[0] == 1:
		A[task[1]-1] = task[2]
		if task[1] == N:
			if A[task[1]-1] % A[task[1]-2] != 0:
				S.add(task[1]-1)
		elif task[1] == 1:
			if 1 < len(A) and A[1]%A[0] != 0:
				S.add(1)
		else:
			index = task[1]-1
			if A[index]%A[index-1] == 0 and A[index+1]%A[index] == 0:
				if index in S:
					S.remove(index)
			elif A[index]%A[index-1] != 0 and A[index+1]%A[index] == 0:
				S.add(index)

			elif A[index]%A[index-1] == 0 and A[index+1]%A[index] != 0:
				if index in S:
					S.remove(index)
				S.add(index+1)
			else:
				S.add(index)
				S.add(index+1)

	else:
		maxInd = 0
		for entry in S:
			if entry > maxInd and entry <= (task[1]-1):
				maxInd = entry
		print(maxInd+1)

	j += 1