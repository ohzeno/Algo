-- https://school.programmers.co.kr/learn/courses/30/lessons/59040
/*
동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요.
이때 고양이를 개보다 먼저 조회해주세요.
*/
# SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = "Cat"
   OR ANIMAL_TYPE = "Dog"
GROUP BY ANIMAL_TYPE
# 고양이를 먼저
ORDER BY ANIMAL_TYPE

/*
where절이 없어도 통과되는데, 이는 테이블에 고양이와 개만 있기 때문이다.
그 조건이 명시되지 않았으므로 where절을 넣어주는게 엄밀한 풀이.
count의 경우 이전에는 ANIMAL_TYPE을 세어줬지만
where, group by가 실행된 후에 count가 실행되므로 *로 바꿔줘도 된다.
*/