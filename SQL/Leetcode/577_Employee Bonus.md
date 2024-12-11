## Problem
[577. Combine Two Tables.](https://leetcode.com/problems/employee-bonus/description/)

### Solution
```sql
SELECT t1.name AS name, t2.bonus AS bonus 
    FROM Employee t1
    LEFT OUTER JOIN Bonus t2 
        ON t1.empId = t2.empID
WHERE bonus < 1000 OR bonus IS NULL;
```
