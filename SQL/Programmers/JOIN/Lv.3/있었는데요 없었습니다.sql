-- https://school.programmers.co.kr/learn/courses/30/lessons/59043
/*
관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다.
보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요.
이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID의 외래 키입니다.
*/
SELECT INS.ANIMAL_ID, INS.NAME  # 양쪽에 다 있는 값 가져올거라 기반 outs해도 됨.
FROM ANIMAL_OUTS OUTS
LEFT JOIN ANIMAL_INS INS
    ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE OUTS.DATETIME < INS.DATETIME  # 보호 시작일보다 입양일이 더 빠른 동물
ORDER BY INS.DATETIME  # 보호 시작일 순