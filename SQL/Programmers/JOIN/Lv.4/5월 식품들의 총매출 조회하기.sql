-- https://school.programmers.co.kr/learn/courses/30/lessons/131117
/*
FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 2022년 5월인 식품들의
식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요.
이때 결과는 총매출을 기준으로 내림차순 정렬해주시고
총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요.
*/
WITH TOTAL_ORDER AS (
    SELECT PRODUCT_ID, SUM(AMOUNT) AS AMOUNT  # 식품별 총 주문량
    FROM FOOD_ORDER
    WHERE DATE_FORMAT(PRODUCE_DATE, '%Y-%m') = '2022-05'
    GROUP BY PRODUCT_ID  # 주문일자 달라도 같은 식품이면 묶기.
)
SELECT PRO.PRODUCT_ID, PRO.PRODUCT_NAME,
       PRO.PRICE * ORD.AMOUNT AS TOTAL_SALES  # 가격 * 주문량 = 총 매출
FROM FOOD_PRODUCT AS PRO
JOIN TOTAL_ORDER AS ORD
    ON PRO.PRODUCT_ID = ORD.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRO.PRODUCT_ID ASC;