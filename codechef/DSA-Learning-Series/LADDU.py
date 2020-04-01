T = int(input())
for _ in range(T):
	[N, origin] = input().split(' ')
	score, divisor = 0, 0
	if origin == 'INDIAN':
		divisor = 200
	else:
		divisor = 400
	for _ in range(int(N)):
		activity = input().split(' ')
		if activity[0] == 'CONTEST_WON':
			score += 300
			if int(activity[1]) <= 20:
				score += (20-int(activity[1]))
		elif activity[0] == 'BUG_FOUND':
			score += int(activity[1])
		elif activity[0] == 'CONTEST_HOSTED':
			score += 50
		elif activity[0] == 'TOP_CONTRIBUTOR':
			score += 300
	print(score//divisor)
