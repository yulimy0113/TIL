### 고양이와 개는 몇 마리 있을까
https://school.programmers.co.kr/learn/courses/30/lessons/59040

```sql
SELECT ANIMAL_TYPE, COUNT(*) count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC;
```
  
  
### 동명 동물 수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/59041

```sql
SELECT NAME, COUNT(*) COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
    HAVING COUNT(*) > 1
ORDER BY NAME;
```
  
  
### 부서별 평균 연봉 조회하기
https://school.programmers.co.kr/learn/courses/30/lessons/284529

```sql
SELECT E.DEPT_ID, D.DEPT_NAME_EN, ROUND(AVG(SAL),0) AVG_SAL
FROM HR_EMPLOYEES E
    JOIN HR_DEPARTMENT D 
    USING(DEPT_ID)
GROUP BY E.DEPT_ID
ORDER BY AVG_SAL DESC;
```
