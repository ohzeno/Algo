-- https://school.programmers.co.kr/learn/courses/30/lessons/59044
/*
아직 입양을 못 간 동물 중,
가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요.
이때 결과는 보호 시작일 순으로 조회해야 합니다.
*/
SELECT INS.NAME, INS.DATETIME  # 입양 못 간 동물이니 보호소 기반.
FROM ANIMAL_INS INS
LEFT JOIN ANIMAL_OUTS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL  # 입양 못 간 동물
ORDER BY INS.DATETIME  # 보호 시작일 순
LIMIT 3  # 3마리만