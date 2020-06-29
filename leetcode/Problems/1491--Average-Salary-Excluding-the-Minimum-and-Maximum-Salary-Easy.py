class Solution:
    def average(self, salary: List[int]) -> float:
        sal = sum(salary)
        sal -= max(salary)
        sal -= min(salary)
        
        return sal/(len(salary)-2)