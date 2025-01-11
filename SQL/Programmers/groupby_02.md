### 진료과별 총 예약 횟수 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/132202

```sql
SELECT MCDP_CD AS 진료과코드, COUNT(PT_NO) AS 5월예약건수
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = '2022'
    AND MONTH(APNT_YMD) = '05'
GROUP BY MCDP_CD
ORDER BY 5월예약건수, 진료과코드;
```
  
  
### 카테고리별 도서 판매량 집계하기
https://school.programmers.co.kr/learn/courses/30/lessons/144855

```sql
SELECT CATEGORY, SUM(SALES) TOTAL_SALES
FROM BOOK_SALES s
    JOIN BOOK b 
    USING(BOOK_ID)
WHERE s.SALES_DATE LIKE '2022-01%'
GROUP BY CATEGORY
ORDER BY CATEGORY;
```
  
  
### 즐겨찾기가 가장 많은 식당 정보 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/131123

```sql
SELECT OG.FOOD_TYPE, REST_ID, REST_NAME, OG.FAVORITES
FROM REST_INFO OG
    INNER JOIN (SELECT FOOD_TYPE, MAX(FAVORITES) OVER (PARTITION BY FOOD_TYPE) MAX_FAV
                FROM REST_INFO) MF
    ON OG.FOOD_TYPE = MF.FOOD_TYPE
        AND OG.FAVORITES = MF.MAX_FAV
GROUP BY REST_NAME
ORDER BY OG.FOOD_TYPE DESC;
```


### 조건에 맞는 사용자와 총 거래금액 조회하기
https://school.programmers.co.kr/learn/courses/30/lessons/164668
```sql
SELECT USER_ID, NICKNAME, SUM(PRICE) TOTAL_SALES
FROM USED_GOODS_BOARD UGB
    JOIN USED_GOODS_USER UGU
    ON UGB.WRITER_ID = UGU.USER_ID
WHERE UGB.STATUS = 'DONE'
GROUP BY USER_ID
    HAVING SUM(PRICE) >= 700000
ORDER BY TOTAL_SALES;
```
