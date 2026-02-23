# https://school.programmers.co.kr/learn/courses/30/lessons/164672
/*
USED_GOODS_BOARD
    BOARD_ID	VARCHAR(5)	FALSE
    WRITER_ID	VARCHAR(50)	FALSE
    TITLE	VARCHAR(100)	FALSE
    CONTENTS	VARCHAR(1000)	FALSE
    PRICE	NUMBER	FALSE
    CREATED_DATE	DATE	FALSE
    STATUS	VARCHAR(10)	FALSE
    VIEWS	NUMBER	FALSE
*/


-- 코드를 입력하세요
SELECT BOARD_ID,
       WRITER_ID,
       TITLE,
       PRICE,
       CASE STATUS
           WHEN 'SALE' THEN '판매중'
           WHEN 'RESERVED' THEN '예약중'
           WHEN 'DONE' THEN '거래완료'
       END AS STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE = '2022-10-05'
ORDER BY BOARD_ID DESC;


/*
String, Date
Lv.2. 현 시점 완료한 사람 21,104명, 정답률 83%
CASE는 엄청 오랜만에 봄.
데이터크립 포매턴는 END를 WHEN이랑 같은 줄에 정렬하는데
아직은 CASE랑 같은 라인이 직관적이지 않나 싶긴 함.
*/
