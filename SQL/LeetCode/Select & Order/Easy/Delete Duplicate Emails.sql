-- https://leetcode.com/problems/delete-duplicate-emails/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Person;
CREATE TABLE Person (Id int, Email varchar(255));
INSERT INTO Person (Id, Email)
VALUES ('1', 'john@example.com'),
       ('2', 'bob@example.com'),
       ('3', 'john@example.com');
/*
Write an SQL query to delete all the duplicate emails,
keeping only one unique email with the smallest id.
Note that you are supposed to write a DELETE statement and not a SELECT one.

After running your script, the answer shown is the Person table.
The driver will first compile and run your piece of code and then show the Person table.
The final order of the Person table does not matter.
*/
DELETE FROM Person
WHERE Id NOT IN (
    SELECT * FROM (  -- DELETE의 서브쿼리는 테이블 수정작업이 허용되지 않기 때문에 아래 쿼리로 수정해서 제한을 우회한다.
        SELECT MIN(Id) AS Id FROM Person GROUP BY Email  -- Email로 그룹화하고 가장 작은 Id를 선택: 중복된 이메일 중 가장 작은 Id를 선택
    ) AS t
);