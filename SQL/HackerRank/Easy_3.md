## Problem 1
[Weather Observation Station 4](https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true)

### Solution
```sql
SELECT COUNT(CITY) - COUNT(DISTINCT(CITY))
FROM STATION;
```


## Problem 2
[Weather Observation Station 6](https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true)

### Solution
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(LEFT(CITY, 1)) in ('a', 'e', 'i', 'o', 'u');
```


## Problem 3
[Weather Observation Station 7](https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true)

### Solution
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(RIGHT(CITY, 1)) in ('a', 'e', 'i', 'o', 'u');
```


## Problem 4
[Weather Observation Station 8](https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true)

### Solution
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(LEFT(CITY, 1)) in ('a', 'e', 'i', 'o', 'u')
    AND LOWER(RIGHT(CITY, 1)) in ('a', 'e', 'i', 'o', 'u');
```


## Problem 5
[Weather Obsercation Station 9](https://www.hackerrank.com/challenges/weather-observation-station-9/problem?isFullScreen=true)

### Solution
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(LEFT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
```


## Problem 6
[Weather Observation Station 10](https://www.hackerrank.com/challenges/weather-observation-station-10/problem?isFullScreen=true)

### Solution
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(RIGHT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
```


## Problem 7
[Weather Observation Station 11](https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true)

### Solution
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(RIGHT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u')
    OR LOWER(LEFT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
```


## Problem 8
[Weather Observation Station 12](https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true)

### Solution
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(RIGHT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u')
    AND LOWER(LEFT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
```
