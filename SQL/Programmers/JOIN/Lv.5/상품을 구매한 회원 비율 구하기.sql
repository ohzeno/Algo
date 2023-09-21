-- https://school.programmers.co.kr/learn/courses/30/lessons/131534
/*
USER_INFO 테이블과 ONLINE_SALE 테이블에서 2021년에 가입한 전체 회원들 중
상품을 구매한 회원수와
상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을
년, 월 별로 출력하는 SQL문을 작성해주세요.
상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림하고,
전체 결과는 년을 기준으로 오름차순 정렬해주시고
년이 같다면 월을 기준으로 오름차순 정렬해주세요.
*/
# # 2021년에 가입한 전체 회원들
# WITH JOINED_2021 AS (SELECT USER_ID
#                      FROM USER_INFO
#                      WHERE YEAR(JOINED) = '2021'),
#      # 2021년에 가입한 회원 중 상품을 구매한 회원들
#      SALES_MEMBER_2021 AS (SELECT SALE.USER_ID, SALE.SALES_DATE
#                            FROM ONLINE_SALE AS SALE
#                                     JOIN JOINED_2021 AS JOINED
#                                          ON SALE.USER_ID = JOINED.USER_ID),
#      # 월별 상품 구매 회원수
#      MONTHLY_BOUGHT AS (SELECT SALES.SALES_DATE              AS DATE,
#                                COUNT(DISTINCT SALES.USER_ID) AS CNT # 그룹 내 중복 제거 후 구매 회원 수
#                         FROM SALES_MEMBER_2021 AS SALES
#                         GROUP BY DATE_FORMAT(SALES.SALES_DATE, '%Y-%m') # 년-월로 그룹화. 단순 월 아님.
#      )
# SELECT YEAR(MONTHLY.DATE)  AS YEAR,
#        MONTH(MONTHLY.DATE) AS MONTH,
#        MONTHLY.CNT         AS PURCHASED_USERS,
#        ROUND(
#                    MONTHLY.CNT / (SELECT COUNT(*) FROM JOINED_2021), # 2021년 가입 회원 중 해당 달에 상품 구매한 회원수 / 2021년 가입 전체 회원 수
#                    1)      AS PURCHASED_RATIO
# FROM MONTHLY_BOUGHT AS MONTHLY
# ORDER BY YEAR ASC, MONTH ASC;
WITH USER_21 AS (SELECT USER_ID
                 FROM USER_INFO
                 WHERE YEAR(JOINED) = 2021),
     BOUGHT AS (SELECT YEAR(OS.SALES_DATE)        AS YEAR,
                       MONTH(OS.SALES_DATE)       AS MONTH,
                       COUNT(DISTINCT OS.USER_ID) AS CNT
                FROM ONLINE_SALE AS OS
                         JOIN USER_21 AS U2
                              ON OS.USER_ID = U2.USER_ID
                GROUP BY YEAR, MONTH)
SELECT YEAR,
       MONTH,
       CNT                                            AS PURCHASED_USERS,
       ROUND(CNT / (SELECT COUNT(*) FROM USER_21), 1) AS PURCHASED_RATIO
FROM BOUGHT
ORDER BY YEAR, MONTH

/*
문제 예시에서 purchased를 puchased라고 적어놓았음. 단어를 제대로 적어도 통과는 됨.
다시 풀면서 코드가 훨씬 간결해졌다.
이전엔 2021년에 가입한 회원 중 상품을 구매한 회원들, 월별 상품 구매 회원수를 따로 테이블로 만들었는데
이번에는 JOIN으로 구매목록에서 YEAR, MONTH로 그룹화 하면서 21년에 가입한 회원만 걸러내어 하나의 테이블로 만들었다.
*/
