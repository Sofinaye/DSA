# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_map = {}
        for emp in employees:
            employee_map[emp.id] = emp
        
        total_importance = 0
        queue = deque([id])
        
        while queue:
            current_id = queue.popleft()
            current_employee = employee_map[current_id]
            total_importance += current_employee.importance
            for subordinate_id in current_employee.subordinates:
                queue.append(subordinate_id)
        
        return total_importance
