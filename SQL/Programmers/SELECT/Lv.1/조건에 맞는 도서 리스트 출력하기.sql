# https://school.programmers.co.kr/learn/courses/30/lessons/144853
/*
BOOK
    Column name Type Nullable Description
    BOOK_ID	INTEGER	FALSE	도서 ID
    CATEGORY	VARCHAR(N)	FALSE	카테고리 (경제, 인문, 소설, 생활, 기술)
    AUTHOR_ID	INTEGER	FALSE	저자 ID
    PRICE	INTEGER	FALSE	판매가 (원)
    PUBLISHED_DATE	DATE	FALSE	출판일
*/


SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문'
  AND YEAR(PUBLISHED_DATE) = 2021
ORDER BY PUBLISHED_DATE ASC;


/*
SELECT
Lv.1. 현 시점 완료한 사람 37,111명, 정답률 87%
DATE_FORMAT는 너무 오랜만이라 기억 안났다.
*/
