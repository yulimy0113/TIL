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


## Problem 2
[The PADS](https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true)

### Solution
```sql
SELECT CONCAT(NAME, '(', SUBSTRING(OCCUPATION, 1, 1), ')')
FROM OCCUPATIONS
ORDER BY NAME;

SELECT CONCAT('There are a total of ', COUNT(NAME), ' ', LOWER(OCCUPATION), 's.')
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(NAME), OCCUPATION; /* AND 는 동일하게 적용되고, comma(,)는 순차적으로 적용된다.*/

```
