import json
from functools import cmp_to_key
from typing import List
from datetime import date

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
    with open(filename) as json_file:
        data = json.load(json_file)
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


def printProblems(problems: List[LeetCodeProblem], count: int = 8):
    for problem in problems:
        if count == 0:
            return
        print('--- Problem ---')
        print('      ID: ', problem.problem_id)
        print('   Title: ', problem.title)
        print('Solution: ', problem.solution)
        count -= 1


def writeToFile(problems: List[LeetCodeProblem], outfile, print_level: bool = True, ac_status: List[str] = ['ac', 'notac', 'na']):
    print(ac_status)
    if print_level:
        # outfile.write(
        # 	'| **ID** | **Title** | **Level** | **Algo Tags** | **DS Tags** | '+
        # 	'**Problem Link** | **Solution Link** | **Solution File** | '+
        # 	'**Best time complexity** | **Additional Notes** |\n'
        # )
        outfile.write(
            '| **Attempted?** | **Is Premium?** | ID | Title | Level | Algo Tags | DS Tags | ' +
            'Problem Link | Solution Link | Solution File | ' +
            'Time complexity | Space complexity | Additional Notes |\n'
        )
        outfile.write('|----|----|----|----|----|----|----|----|----|----|----|\n')
    else:
        outfile.write(
            '| **Attempted?** | **Is Premium?** | **ID** | **Title** | **Algo Tags** | **DS Tags** | ' +
            '**Problem Link** | **Solution Link** | **Solution File** | ' +
            '**Time complexity** | **Space complexity** | **Additional Notes** |\n'
        )
        outfile.write('|----|----|----|----|----|----|----|----|----|\n')
    problem_link_prefix = 'https://leetcode.com/problems/'  # '[Link](https://leetcode.com/problems/'
    problem_link_suffix = '/'  # '/)'
    problem_sol_link_suffix = '/solution/'  # '/solution/)'
    for problem in problems:
        problem_id = str(problem.problem_id)  # str(problem.id).zfill(4)
        problem_status = problem.status
        problem_premium = 'Yes' if problem.is_premium is True else ''
        problem_title = problem.title
        problem_link = problem_link_prefix + problem.slug + problem_link_suffix
        problem_level = levels[problem.difficulty - 1]
        problem_sol_link = \
            '' \
            if problem.solution is None \
            else problem_link_prefix + problem.solution + problem_sol_link_suffix
        algo_tags = []
        ds_tags = []
        time_complexity = ''
        space_complexity = ''
        additional_notes = ''
        problem_sol_file = ''
        if problem_status in ac_status:
            if print_level:
                outfile.write(
                    '| ' +
                    problem_status + ' | ' +
                    problem_premium + ' | ' +
                    problem_id + ' | ' +
                    problem_title + ' | ' +
                    problem_level + ' | ' +
                    ", ".join(repr(e) for e in algo_tags) + ' | ' +
                    ", ".join(repr(e) for e in ds_tags) + ' | ' +
                    problem_link + ' | ' +
                    problem_sol_link + ' | ' +
                    problem_sol_file + ' | ' +
                    time_complexity + ' | ' +
                    space_complexity + ' | ' +
                    additional_notes + ' |\n'
                )
            else:
                outfile.write(
                    '| ' +
                    problem_status + ' | ' +
                    problem_premium + ' | ' +
                    problem_id + ' | ' +
                    problem_title + ' | ' +
                    ", ".join(repr(e) for e in algo_tags) + ' | ' +
                    ", ".join(repr(e) for e in ds_tags) + ' | ' +
                    problem_link + ' | ' +
                    problem_sol_link + ' | ' +
                    problem_sol_file + ' | ' +
                    time_complexity + ' | ' +
                    space_complexity + ' | ' +
                    additional_notes + ' |\n'
                )


def createBibString(problem: LeetCodeProblem):
    url = 'https://leetcode.com/problems/' + problem.slug
    bib = '@misc{'
    bib += 'leetcode:problems:algorithms:' + problem.slug + ',\n'
    bib += '\tauthor={{}},\n'
    bib += '\ttitle={{' + str(problem.problem_id) + '. ' + problem.title + '}},\n'
    bib += '\tnote={\\url{' + url + '}. Last accessed: ' + date.today().strftime("%d %B, %Y") + '},\n'
    bib += '\thowpublished={{LeetCode}},\n'
    bib += '\turl={' + url + '/},\n'
    bib += '}\n\n'
    return bib


def writeBibFile(problems: List[LeetCodeProblem], filename: str = 'leetcode.bib'):
    with open(filename, 'w') as outfile:
        for problem in problems:
            bib_string = createBibString(problem)
            outfile.write(bib_string)


def completeTodo(problems: List[LeetCodeProblem], filename: str = 'TODO.md'):
    with open(filename, 'w') as outfile:
        outfile.write('# TODO\n\n')
        outfile.write('## Problems\n\n')
        writeToFile(problems, outfile)


def attempted(problems: List[LeetCodeProblem], filename: str = 'TODO.md'):
    with open(filename, 'w') as outfile:
        outfile.write('# TODO\n\n')
        outfile.write('## Problems\n\n')
        writeToFile(problems, outfile, ac_status=['ac'])


def levelWiseTodo(problems: List[LeetCodeProblem], filename: str = 'CAT-TODO.md'):
    easy = []
    medium = []
    hard = []
    for problem in problems:
        if problem.difficulty == 1:
            easy.append(problem)
        elif problem.difficulty == 2:
            medium.append(problem)
        elif problem.difficulty == 3:
            hard.append(problem)
        else:
            print('I dont know this level')
    with open(filename, 'w') as outfile:
        outfile.write('# TODO\n\n')
        outfile.write('## Problems\n\n')
        outfile.write('### Easy\n\n')
        writeToFile(easy, outfile, False)
        outfile.write('\n### Medium\n\n')
        writeToFile(medium, outfile, False)
        outfile.write('\n### Hard\n\n')
        writeToFile(hard, outfile, False)


if __name__ == "__main__":
    algorithm_problems = readProblems('leetcode-output-bunny.json')
    algorithm_problems = sorted(algorithm_problems, key=cmp_to_key(compare))
    algorithm_problems = algorithm_problems[::-1]
    printProblems(algorithm_problems)
    print('Writing to EXCEL.md')
    completeTodo(algorithm_problems, 'EXCEL.md')
    print('Writing to ATTEMPTED.md')
    attempted(algorithm_problems, 'ATTEMPTED.md')
