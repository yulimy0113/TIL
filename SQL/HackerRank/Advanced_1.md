## Problem 1
[Type of Triangle](https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true)

### Solution
```sql
SELECT CASE WHEN (A = B AND B = C) THEN 'Equilateral'
    WHEN A = B AND A+B > C AND A != C THEN 'Isosceles'
    WHEN A = C AND A+C > B AND A != B THEN 'Isosceles'
    WHEN C = B AND C+B > A AND A != C THEN 'Isosceles'
    WHEN A != B AND B != C AND A+B > C THEN 'Scalene'
    ELSE 'Not A Triangle'
    END AS TRITYPE
FROM TRIANGLES;
```
