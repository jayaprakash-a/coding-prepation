T = int(input())
for _ in range(T):
	cars = int(input())
	speeds = input().split(' ')
	minSpeed = int(speeds[0])
	count = 1
	for i in range(cars-1):
		speed = int(speeds[i+1])
		if speed < minSpeed:
			count += 1
			minSpeed = speed

	print(count)
