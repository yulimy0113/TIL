## Problem
[182. Duplicate Emails.](https://leetcode.com/problems/duplicate-emails/description/)

### Solution
```sql
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(id) > 1;
```
