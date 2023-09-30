-- https://leetcode.com/problems/fix-names-in-a-table/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Users;
Create table Users (user_id int, name varchar(40));
insert into Users (user_id, name)
values ('1', 'aLice'),
       ('2', 'bOB');
/*
Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.
Return the result table ordered by user_id.
*/
SELECT user_id, CONCAT(
    UPPER(LEFT(name, 1)),
    LOWER(SUBSTRING(name, 2))
) AS name
FROM Users
ORDER BY user_id;