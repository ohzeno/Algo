# https://school.programmers.co.kr/learn/courses/30/lessons/131697
/*
PRODUCT
    PRODUCT_ID	INTEGER	FALSE
    PRODUCT_CODE	VARCHAR(8)	FALSE
    PRICE	INTEGER	FALSE
*/


-- 코드를 입력하세요
SELECT PRICE AS MAX_PRICE
FROM PRODUCT
ORDER BY PRICE DESC
LIMIT 1;


/*
SUM, MAX, MIN
Lv.1. 현 시점 완료한 사람 35,978명, 정답률 92%
*/