-- https://school.programmers.co.kr/learn/courses/30/lessons/131533
/*
PRODUCT 테이블과 OFFLINE_SALE 테이블에서
상품코드 별 매출액(판매가 * 판매량) 합계를 출력하는 SQL문을 작성해주세요.
결과는 매출액을 기준으로 내림차순 정렬해주시고
매출액이 같다면 상품코드를 기준으로 오름차순 정렬해주세요.
*/
SELECT PRO.PRODUCT_CODE,
       SUM(PRO.PRICE * OFF.SALES_AMOUNT) AS SALES
FROM PRODUCT AS PRO
         JOIN OFFLINE_SALE AS OFF # JOIN = INNER JOIN 양쪽 테이블에서 일치하는 데이터만 가져옴. LEFT JOIN은 오른쪽 테이블에 값 없으면 NULL로 출력.
              ON PRO.PRODUCT_ID = OFF.PRODUCT_ID
# GROUP BY PRO.PRODUCT_CODE # 상품코드 별
GROUP BY OFF.PRODUCT_ID
# ORDER BY SALES DESC, PRO.PRODUCT_CODE ASC;
ORDER BY SALES DESC, PRO.PRODUCT_CODE;


/*
다시 풀면서 GROUP BY만 바뀌었다.
*/
