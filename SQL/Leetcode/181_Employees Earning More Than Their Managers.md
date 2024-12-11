## Problem
[181. Employees Earning More Than Their Managers.](https://leetcode.com/problems/employee-bonus/description/)

### Solution
```sql
SELECT t1.name AS Employee
FROM Employee t1
  JOIN Employee t2
  ON t1.managerId = t2.id
WHERE t1.salary > t2.salary;
```
