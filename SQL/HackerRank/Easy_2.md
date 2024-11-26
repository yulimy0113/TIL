## Problem 1
[Weather Observation Station 1](https://www.hackerrank.com/challenges/weather-observation-station-1/problem?isFullScreen=true)

## Solution
```sql
SELECT CITY, STATE
FROM STATION;
```


## Problem 2
[Weather Observation Station 3](https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true)

## Solution
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID, 2)=0;
```


## Problem 3
[Weather Observation Station 5](https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true)

## Solution
```sql
SELECT CITY, LENGTH(CITY) LEN
FROM STATION
ORDER BY LEN DESC, CITY ASC
LIMIT 1;

SELECT CITY, LENGTH(CITY) LEN
FROM STATION
ORDER BY LEN ASC, CITY ASC
LIMIT 1;
```
