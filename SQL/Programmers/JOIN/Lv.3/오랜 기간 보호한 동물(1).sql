-- https://school.programmers.co.kr/learn/courses/30/lessons/59044
/*
아직 입양을 못 간 동물 중,
가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요.
이때 결과는 보호 시작일 순으로 조회해야 합니다.
*/
SELECT INS.NAME, INS.DATETIME # 입양 못 간 동물이니 보호소 기반.
FROM ANIMAL_INS AS INS
         LEFT JOIN ANIMAL_OUTS AS OUTS
                   ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL # 입양 못 간 동물
# ORDER BY INS.DATETIME # 보호 시작일 순
ORDER BY DATETIME
LIMIT 3 # 3마리만


/*
다시 풀면서 ORDER BY만 바뀌었다.
OUTS에도 DATETIME이 존재하니 원래는 INS.으로 특정해줘야 하지만
이 경우는 OUTS에 없는 것만 조회하니 DATETIME은 INS의 컬럼으로 특정된다.
*/