from collections import Counter
def get_answer(country_map, chef_map):
	chef = chef_map.most_common(1)
	chef_name = chef[0][0]
	count = chef[0][1]
	for entry in chef_map.keys():
		if count == chef_map[entry]:
			chef_name = min(chef_name, entry)

	country = country_map.most_common(1)
	country_name = country[0][0]
	count = country[0][1]
	for entry in country_map.keys():
		if count == country_map[entry]:
			country_name = min(country_name, entry)

	print(country_name)
	print(chef_name)

def process_input(N, M):
	country_map = Counter()
	chef_country = Counter()
	chef_map = Counter()
	for _ in range(N):
		[chef, country] = input().strip().split(' ')
		chef_map[chef] = 0
		country_map[country] = 0
		chef_country[chef] = country

	for _ in range(M):
		chef = input().strip()
		chef_map[chef] += 1
		country_map[chef_country[chef]] += 1

	return country_map, chef_map


[N, M] = [int(i) for i in input().strip().split(' ')]
country_map, chef_map = process_input(N, M)
get_answer(country_map, chef_map)