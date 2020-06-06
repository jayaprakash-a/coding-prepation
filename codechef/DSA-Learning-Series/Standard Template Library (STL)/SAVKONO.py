import heapq as hp
def get_answer(Z, powers):
	powers = [-1*power for power in powers]
	hp.heapify(powers)
	count = 0
	while Z and powers:
		count += 1
		strength = hp.heappop(powers)
		Z += strength
		if Z <= 0:
			return str(count)
		strength = abs(strength)//2
		if strength:
			hp.heappush(powers, -1*strength)
	if Z:
		return "Evacuate"
	return str(count)

T = int(input())
for _ in range(T):
	[N, Z] = [int(i) for i in input().strip().split()]
	powers = [int(i) for i in input().strip().split()]
	print(get_answer(Z, powers))
