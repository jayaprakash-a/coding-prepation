import glob

import json
from functools import cmp_to_key
from typing import List
from datetime import date
import codecs
levels = ['Easy', 'Medium', 'Hard']


class LeetCodeProblem:

	def __int__(self, problem_id: int,
				title: str = '', slug: str = '',
				solution: str = '', difficulty: int = 0,
				is_premium: bool = False,
				status: str = ''):
		self.problem_id = problem_id
		self.title = title
		self.slug = slug
		self.solution = solution
		self.difficulty = difficulty
		self.status = status
		self.is_premium = is_premium


def readProblems(filename: str):
	problems = []	

	data = json.load(codecs.open(filename, 'r', 'utf-8-sig'))
	# print(data['stat_status_pairs'])
	for item in data['stat_status_pairs']:
		problem = LeetCodeProblem()
		problem.problem_id = int(item['stat']['frontend_question_id'])
		problem.title = item['stat']['question__title']
		problem.slug = item['stat']['question__title_slug']
		problem.solution = item['stat']['question__article__slug']
		problem.difficulty = int(item['difficulty']['level'])
		problem.status = 'na' if item['status'] is None else item['status']
		problem.is_premium = item['paid_only']
		problems.append(problem)
	return problems


# Reference: https://stackoverflow.com/questions/5213033/sort-list-of-list-with-custom-compare-function-in-python
def compare(item1: LeetCodeProblem, item2: LeetCodeProblem):
	# print(item1.id, ' ', item2.id, ' ', item1.id-item2.id)
	return item1.problem_id - item2.problem_id

def getAttemptedProblems(problems: List[LeetCodeProblem]):
	attempted_problems = []
	for problem in problems:
		if problem.status == 'ac':
			attempted_problems.append(problem)
	return attempted_problems



if __name__ == "__main__":
	algorithm_problems = readProblems('leetcode-output-bunny.json')
	algorithm_problems = sorted(algorithm_problems, key=cmp_to_key(compare))
	algorithm_problems = algorithm_problems[::-1]
	attempted_problems = getAttemptedProblems(algorithm_problems) 
	attempted_problems_ids = []
	for problem in algorithm_problems:
		if problem.status == 'ac':
			attempted_problems_ids.append(problem.problem_id)
	
	written_problems = glob.glob("../Problems/*.py")
	# written_problems.pop()
	written_problems_ids = []
	for problem in written_problems:
		filename = problem.replace('../Problems/', '')
		if filename != "rename.py" and filename != "UpdateLists.py" and filename != "UpdateProblemTags.py":
			written_problems_ids.append(int(filename.split('--')[0]))
	print(len(attempted_problems_ids), len(written_problems_ids))
	missing = []
	for problem in attempted_problems_ids:
		if problem not in written_problems_ids:
			missing.append(problem)
	print(missing)
