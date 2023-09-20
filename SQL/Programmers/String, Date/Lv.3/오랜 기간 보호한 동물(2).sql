-- https://school.programmers.co.kr/learn/courses/30/lessons/59411
/*
입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의
아이디와 이름을 조회하는 SQL문을 작성해주세요.
이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.
*/
SELECT OUTS.ANIMAL_ID, OUTS.NAME  # 입양간 동물이니 OUTS기반
FROM ANIMAL_OUTS AS OUTS
LEFT JOIN ANIMAL_INS AS INS
       ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
ORDER BY OUTS.DATETIME - INS.DATETIME DESC  # 보호기간은 입양날짜 - 보호날짜
LIMIT 2;

