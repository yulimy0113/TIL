### 재구매가 일어난 상품과 회원 리스트 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/131536

```sql
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
    HAVING COUNT(*) > 1
ORDER BY USER_ID, PRODUCT_ID DESC;
```


### 업그레이드된 아이템 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/273711

```sql
SELECT t.ITEM_ID, i.ITEM_NAME, i.RARITY
FROM ITEM_TREE t
    INNER JOIN ITEM_INFO i
    ON t.ITEM_ID = i.ITEM_ID
WHERE t.PARENT_ITEM_ID IN (SELECT ITEM_ID
                          FROM ITEM_INFO
                          WHERE RARITY = 'RARE')
ORDER BY ITEM_ID DESC;
```


### 대장균들의 자식의 수 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/299305

```sql
SELECT A.ID, IFNULL(COUNT(B.ID), 0) CHILD_COUNT
FROM ECOLI_DATA A
    LEFT JOIN ECOLI_DATA B
    ON A.ID = B.PARENT_ID
GROUP BY A.ID;
```
