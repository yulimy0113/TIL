### 성분으로 구분한 아이스크림 총 주문량
https://school.programmers.co.kr/learn/courses/30/lessons/133026

```sql
SELECT i.INGREDIENT_TYPE INGREDIENT_TYPE, SUM(h.TOTAL_ORDER) TOTAL_ORDER
FROM FIRST_HALF h
    LEFT JOIN ICECREAM_INFO i USING(FLAVOR)
GROUP BY i.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER;
```
  
  
### 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/151137

```sql
SELECT CAR_TYPE, COUNT(*) CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE FIND_IN_SET('통풍시트', OPTIONS)
    OR FIND_IN_SET('열선시트', OPTIONS)
    OR FIND_IN_SET('가죽시트', OPTIONS)
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE;
```
  
  
### 자동차 대여 기록에서 대여중/대여 가능 여부 구분하기
https://school.programmers.co.kr/learn/courses/30/lessons/157340

```sql
SELECT CAR_ID,
    CASE WHEN CAR_ID IN (SELECT DISTINCT CAR_ID
                         FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                         WHERE START_DATE <= '2022-10-16'
                            AND END_DATE >= '2022-10-16') THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;

--- OR

SELECT CAR_ID,
    CASE WHEN MAX('2022-10-16' BETWEEN START_DATE AND END_DATE) = 1
         THEN '대여중'
         ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;    
```


### 대여횟수가 많은 자동차들의 월별 대여 횟수 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/151139
```sql
WITH MONTHLY_RECORD AS(SELECT MONTH(START_DATE) MONTH, CAR_ID, COUNT(*) RECORDS
                       FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                       WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
                       GROUP BY CAR_ID, MONTH(START_DATE))
    , TOTAL_COUNT AS (SELECT CAR_ID 
                      FROM MONTHLY_RECORD
                      GROUP BY CAR_ID
                         HAVING SUM(RECORDS) > 4)
SELECT MONTH, CAR_ID, RECORDS
FROM MONTHLY_RECORD
    INNER JOIN TOTAL_COUNT USING(CAR_ID)
ORDER BY MONTH ASC, CAR_ID DESC;
```
