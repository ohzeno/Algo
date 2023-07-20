-- https://school.programmers.co.kr/learn/courses/30/lessons/59410
/*
천재지변으로 인해 일부 데이터가 유실되었습니다.
입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의
ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID의 외래 키입니다.
*/
SELECT OUTS.ANIMAL_ID, OUTS.NAME  # 입양 간 기록이 있으므로 OUT 기반
FROM ANIMAL_OUTS OUTS
LEFT JOIN ANIMAL_INS INS
    ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL  # INS는 추가 테이블이므로 보호소에 들어온 기록이 없으면 NULL
ORDER BY OUTS.ANIMAL_ID