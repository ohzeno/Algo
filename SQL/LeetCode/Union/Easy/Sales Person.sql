-- https://leetcode.com/problems/sales-person/?envType=study-plan&id=sql-i
Create table If Not Exists SalesPerson (sales_id int, name varchar(255), salary int, commission_rate int, hire_date date);
Create table If Not Exists Company (com_id int, name varchar(255), city varchar(255));
Create table If Not Exists Orders (order_id int, order_date date, com_id int, sales_id int, amount int);
Truncate table SalesPerson;
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
VALUES ('1', 'John', '100000', '6', '2006-04-01'),
       ('2', 'Amy', '12000', '5', '2010-05-01'),
       ('3', 'Mark', '65000', '12', '2008-12-25'),
       ('4', 'Pam', '25000', '25', '2005-01-01'),
       ('5', 'Alex', '5000', '10', '2007-02-03');
Truncate table Company;
insert into Company (com_id, name, city)
values ('1', 'RED', 'Boston'),
       ('2', 'ORANGE', 'New York'),
       ('3', 'YELLOW', 'Boston'),
       ('4', 'GREEN', 'Austin');
Truncate table Orders;
insert into Orders (order_id, order_date, com_id, sales_id, amount)
values ('1', '2014-01-01', '3', '4', '10000'),
       ('2', '2014-02-01', '4', '5', '5000'),
       ('3', '2014-03-01', '1', '1', '50000'),
       ('4', '2014-04-01', '1', '4', '25000');
/*
Write an SQL query to report the
names of all the salespersons
who did not have any orders related to the company with the name "RED".
Return the result table in any order.
*/
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (  # red 관련 주문이 있는 테이블에 존재하지 않는 sales_id
    SELECT O.sales_id
    FROM Orders AS O
    JOIN Company AS C  # where가 있어서 left join해도 결과는 같음.
       on O.com_id = C.com_id
    WHERE C.name = 'RED'
);
/*
LeetCode Easy
처음엔 with로 테이블을 둘이나 만들어서 풀었는데
다른 풀이를 보니 join으로 더 간결하게 풀 수 있어서 바꿨다.
*/
