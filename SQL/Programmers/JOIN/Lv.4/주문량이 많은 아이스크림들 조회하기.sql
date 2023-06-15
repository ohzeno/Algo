-- https://school.programmers.co.kr/learn/courses/30/lessons/133027
/*
7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이
큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.
*/
WITH TOTAL_HALF AS (  # 각 테이블 매출 맛별로 정리
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM FIRST_HALF
    GROUP BY FLAVOR
), TOTAL_JULY AS (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM JULY
    GROUP BY FLAVOR
)
SELECT HALF.FLAVOR
FROM TOTAL_HALF AS HALF
JOIN TOTAL_JULY AS JULY
    ON HALF.FLAVOR = JULY.FLAVOR
ORDER BY HALF.TOTAL_ORDER + JULY.TOTAL_ORDER DESC  # 상반기 + 7월 매출 합계 순위대로
LIMIT 3