# https://school.programmers.co.kr/learn/courses/30/lessons/132201
/*
PATIENT
    PT_NO	VARCHAR(10)	FALSE
    PT_NAME	VARCHAR(20)	FALSE
    GEND_CD	VARCHAR(1)	FALSE
    AGE	INTEGER	FALSE
    TLNO	VARCHAR(50)	TRUE
*/


SELECT PT_NAME, PT_NO, GEND_CD, AGE,
       COALESCE(TLNO, 'NONE')
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME ASC;


/*
SELECT
Lv.1. 현 시점 완료한 사람 39,832명, 정답률 91%
COALESCE는 합친다는 뜻
coalesce (into something) to come together to form one larger group, substance, etc.
NULL 대체 패턴에서 자주 쓰인다는 듯. 처음봤다.
*/
