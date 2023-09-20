-- https://school.programmers.co.kr/learn/courses/30/lessons/133027
/*
7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이
큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.
*/
# WITH TOTAL_HALF AS ( # 각 테이블 매출 맛별로 정리
#     SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
#     FROM FIRST_HALF
#     GROUP BY FLAVOR),
#      TOTAL_JULY AS (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
#                     FROM JULY
#                     GROUP BY FLAVOR)
# SELECT HALF.FLAVOR
# FROM TOTAL_HALF AS HALF
#          JOIN TOTAL_JULY AS JULY
#               ON HALF.FLAVOR = JULY.FLAVOR
# ORDER BY HALF.TOTAL_ORDER + JULY.TOTAL_ORDER DESC # 상반기 + 7월 매출 합계 순위대로
# LIMIT 3;

WITH JUL_ORD AS (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
                 FROM JULY
                 GROUP BY FLAVOR)
SELECT FH.FLAVOR
FROM FIRST_HALF AS FH
         JOIN JUL_ORD AS JUL
              ON FH.FLAVOR = JUL.FLAVOR
ORDER BY (FH.TOTAL_ORDER + JUL.TOTAL_ORDER) DESC
LIMIT 3


/*
다시 풀면서 WITH문이 하나로 줄었다.
7월 매출의 FLAVOR가 상반기 FLAVOR의 외래키라고 하고
7월에만 중복 언급이 있어서 상반기의 FLAVOR는 중복이 없다고 가정했다.
*/