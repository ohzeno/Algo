-- https://school.programmers.co.kr/learn/courses/30/lessons/144854
/*
'경제' 카테고리에 속하는 도서들의
도서 ID(BOOK_ID), 저자명(AUTHOR_NAME), 출판일(PUBLISHED_DATE) 리스트를 출력하는 SQL문을 작성해주세요.
결과는 출판일을 기준으로 오름차순 정렬해주세요.
*/
SELECT BOOK.BOOK_ID,
       AUTHOR.AUTHOR_NAME,
       DATE_FORMAT(BOOK.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
         JOIN AUTHOR
              ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
WHERE BOOK.CATEGORY = '경제'
ORDER BY BOOK.PUBLISHED_DATE;

/*
join 복습에 좋은 쉬운 난이도의 문제.
포맷만 조금 달라져서 가독성이 올라갔다.
*/
