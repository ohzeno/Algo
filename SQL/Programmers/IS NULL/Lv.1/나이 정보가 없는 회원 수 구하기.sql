# https://school.programmers.co.kr/learn/courses/30/lessons/131528
/*
USER_INFO
    USER_ID	INTEGER	FALSE
    GENDER	TINYINT(1)	TRUE
    AGE	INTEGER	TRUE
    JOINED	DATE	FALSE
*/


SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;


/*
IS NULL
Lv.1. 현 시점 완료한 사람 34,156명, 정답률 92%
*/
