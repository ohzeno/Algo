# https://school.programmers.co.kr/learn/courses/30/lessons/133024
/*
FIRST_HALF
    NAME        TYPE        NULLABLE
    SHIPMENT_ID INT(N)      FALSE
    FLAVOR      VARCHAR(N)  FALSE
    TOTAL_ORDER INT(N)      FALSE
*/


-- 코드를 입력하세요
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;


/*
SELECT
Lv.1. 현 시점 완료한 사람 40,444명, 정답률 91%
*/
