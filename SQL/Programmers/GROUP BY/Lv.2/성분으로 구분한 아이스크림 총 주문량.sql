# https://school.programmers.co.kr/learn/courses/30/lessons/133026
/*
FIRST_HALF
    SHIPMENT_ID	INT(N)	FALSE
    FLAVOR	VARCHAR(N)	FALSE
    TOTAL_ORDER	INT(N)	FALSE
ICECREAM_INFO
    FLAVOR	VARCHAR(N)	FALSE
    INGREDIENT_TYPE	VARCHAR(N)	FALSE
*/


-- 코드를 입력하세요
SELECT II.INGREDIENT_TYPE,
       SUM(FH.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF AS FH
         JOIN ICECREAM_INFO AS II
             ON FH.FLAVOR = II.FLAVOR
GROUP BY II.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC;


/*
GROUP BY
Lv.2. 현 시점 완료한 사람 28,523명, 정답률 88%
II.FLAVOR는 FH.FLAVOR의 외래키이므로 INNER든 LEFT든 상관없음.
JOIN은 INNER JOIN임.
어느쪽이든 상관없어서 평소랑 달리 INNER 표기 뺌.
이 문제가 어려운건 아니지만
상대적으로 GROUP BY는 기본적으로 다른 카테고리의 같은 Lv보다 어렵게 느껴짐.
SUM Lv.2는 간단하지만 GROUP BY Lv.2는 다른 카테고리 개념을 포함하는 느낌.
여기도 JOIN, SUM이 기본적으로 포함됨.
*/
