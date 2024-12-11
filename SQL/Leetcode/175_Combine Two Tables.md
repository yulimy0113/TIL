## Problem
[175. Combine Two Tables.](https://leetcode.com/problems/combine-two-tables/description/?envType=problem-list-v2&envId=database)

### Solution
```sql
SELECT t1.firstName as firstName, t1.lastName as lastName, t2.city as city, t2.state as state
    FROM Person t1
    LEFT JOIN Address t2
        ON t1.personId = t2.personId
    ;
```
