## Problem
[183. Customers Who Never Order.](https://leetcode.com/problems/customers-who-never-order/description/)

### Solution
```sql
SELECT t1.name Customers
FROM Customers t1
    LEFT JOIN Orders t2
    ON t1.id = t2.customerId
WHERE t2.customerId IS NULL;
```
