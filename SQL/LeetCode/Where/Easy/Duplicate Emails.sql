-- https://leetcode.com/problems/duplicate-emails/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Person;
Create table Person (id int, email varchar(255));
insert into Person (id, email)
values ('1', 'a@b.com'),
       ('2', 'c@d.com'),
       ('3', 'a@b.com');
/*
Write an SQL query to report all the duplicate emails.
Note that it's guaranteed that the email field is not NULL.
Return the result table in any order.
*/
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;  # group by로 만들어진 테이블에서 count가 1보다 큰 것만 출력