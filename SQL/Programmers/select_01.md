### 서울에 위치한 식당 목록 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/131118

```sql
SELECT i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, ROUND(AVG(r.REVIEW_SCORE), 2) SCORE
FROM REST_INFO i
    RIGHT JOIN REST_REVIEW r
    ON i.REST_ID = r.REST_ID
WHERE LEFT(ADDRESS, 2) = '서울'
GROUP BY i.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC;
```


### 오프라인/온라인 판매 데이터 통합하기
https://school.programmers.co.kr/learn/courses/30/lessons/131537

```sql
WITH SALES AS (SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
               FROM ONLINE_SALE
               WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 3
              UNION
               SELECT SALES_DATE, PRODUCT_ID, NULL USER_ID, SALES_AMOUNT
               FROM OFFLINE_SALE
               WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 3
              )    
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d'), PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM SALES
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;
```


### 3월에 태어난 여성 회원 목록 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/131120

```sql
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3 AND TLNO IS NOT NULL AND GENDER = 'W'
ORDER BY MEMBER_ID;
```
