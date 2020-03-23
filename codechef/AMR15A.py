def main():
	T = int(input())
	odd, even = 0, 0
	# for i in range(T):
	inputStream = input()
	for x in inputStream.split():
		if int(x)%2 == 0:
			even += 1
		else:
			odd += 1
	if even > odd:
		print("READY FOR BATTLE")
	else:
		print("NOT READY")

if __name__ == '__main__':
	main()