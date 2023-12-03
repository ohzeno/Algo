-- https://leetcode.com/problems/sales-analysis-iii/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Sales;
Create table Product (product_id int, product_name varchar(10), unit_price int);
Create table Sales (seller_id int, product_id int, buyer_id int, sale_date date, quantity int, price int);
insert into Product (product_id, product_name, unit_price)
values ('1', 'S8', '1000'),
       ('2', 'G4', '800'),
       ('3', 'iPhone', '1400');
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price)
values ('1', '1', '1', '2019-01-21', '2', '2000'),
       ('1', '2', '2', '2019-02-17', '1', '800'),
       ('2', '2', '3', '2019-06-02', '1', '800'),
       ('3', '3', '4', '2019-05-13', '2', '2800');
/*
Write an SQL query that reports the products that were only sold in the first quarter of 2019.
That is, between 2019-01-01 and 2019-03-31 inclusive.
Return the result table in any order.
*/
SELECT P.product_id, P.product_name
FROM Product AS P
JOIN Sales AS S
       ON P.product_id = S.product_id
GROUP BY P.product_id
HAVING MIN(S.sale_date) >= '2019-01-01' AND
       MAX(S.sale_date) <= '2019-03-31';
/*
LeetCode Easy.
처음에는 JOIN을 사용하지 않고,
Sales 테이블에서 19년 1분기 테이블, 19년 1분기가 아닌 테이블을 나누어
19년 1분기에 포함되고 19년 1분기가 아닐 때 포함되지 않는 id를 찾았다.
Easy치고 쿼리가 길다고 생각했는데
HAVING과 MIN, MAX를 사용하면 쉽게 풀 수 있었다.
*/