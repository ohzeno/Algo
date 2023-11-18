-- https://leetcode.com/problems/combine-two-tables/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Address;
Create table Person (personId int, firstName varchar(255), lastName varchar(255));
Create table Address (addressId int, personId int, city varchar(255), state varchar(255));
insert into Person (personId, lastName, firstName)
values ('1', 'Wang', 'Allen'),
       ('2', 'Alice', 'Bob');
insert into Address (addressId, personId, city, state)
values ('1', '2', 'New York City', 'New York'),
       ('2', '3', 'Leetcode', 'California');
/*
Write an SQL query to report the
first name, last name, city, and state of each person in the Person table.
If the address of a personId is not present in the Address table, report null instead.
Return the result table in any order.
*/
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person AS p
LEFT JOIN Address AS a  # 주소테이블에 없으면 null
       ON p.personId = a.personId;