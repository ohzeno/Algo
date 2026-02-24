# https://school.programmers.co.kr/learn/courses/30/lessons/131115
/*
FOOD_PRODUCT
    PRODUCT_ID	VARCHAR(10)	FALSE
    PRODUCT_NAME	VARCHAR(50)	FALSE
    PRODUCT_CD	VARCHAR(10)	TRUE
    CATEGORY	VARCHAR(10)	TRUE
    PRICE	NUMBER	TRUE
*/


-- 코드를 입력하세요
SELECT * FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)


/*
SUM, MAX, MIN
Lv.2. 현 시점 완료한 사람 39,110명, 정답률 92%
오랜만이라 ALL, *가 존재하는지 기억나지 않아서 다 실행해봤다.
*/
