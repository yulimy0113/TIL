### 조건에 맞는 개발자 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/276034

```sql
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE NAME IN ('Python', 'C#'))
ORDER BY ID;

-- OR

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE ID IN (SELECT DISTINCT D.ID
             FROM DEVELOPERS D
             JOIN SKILLCODES S
             ON D.SKILL_CODE & S.CODE = S.CODE
             WHERE S.NAME = 'C#' OR S.NAME = 'Python')
ORDER BY ID;
```


### 특정 물고기를 잡은 총 수 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/298518

```sql
SELECT COUNT(ID) FISH_COUNT
FROM FISH_INFO i
LEFT JOIN FISH_NAME_INFO n
ON i.FISH_TYPE = n.FISH_TYPE
WHERE n.FISH_NAME IN ('BASS', 'SNAPPER');
```


### 대장균의 크기에 따라 분류하기 1
https://school.programmers.co.kr/learn/courses/30/lessons/299307

```sql
SELECT ID,
        CASE WHEN SIZE_OF_COLONY <= 100
            THEN 'LOW'
            WHEN SIZE_OF_COLONY > 100 AND SIZE_OF_COLONY <= 1000
            THEN 'MEDIUM'
            WHEN SIZE_OF_COLONY > 1000
            THEN 'HIGH'
        END AS SIZE
FROM ECOLI_DATA
ORDER BY ID;
```
