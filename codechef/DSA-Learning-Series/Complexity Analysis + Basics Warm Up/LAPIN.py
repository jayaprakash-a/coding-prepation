T = int(input())

for i in range(T):
	word = input()
	index = len(word)//2
	if len(word)%2 == 0:
		if sorted(word[:index]) == sorted(word[index:]):
			print("YES")
		else:
			print("NO")
	else:
		if sorted(word[:index]) == sorted(word[index+1:]):
			print("YES")
		else:
			print("NO")
