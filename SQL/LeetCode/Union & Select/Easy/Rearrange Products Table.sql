-- https://leetcode.com/problems/rearrange-products-table/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Products;
Create table Products (product_id int, store1 int, store2 int, store3 int);
insert into Products (product_id, store1, store2, store3)
values ('0', '95', '100', '105'),
       ('1', '70', NULL, '80');
/*
Write an SQL query to rearrange the Products table so that each row has (product_id, store, price).
If a product is not available in a store,
do not include a row with that product_id and store combination in the result table.
Return the result table in any order.
*/
SELECT product_id, 'store1' AS store, store1 AS price  # product_id, store, price를 컬럼으로 하는 테이블 생성. store1에 한해서.
FROM Products WHERE store1 IS NOT NULL  # store1이 NULL이 아닌 경우에만
UNION
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products WHERE store3 IS NOT NULL
ORDER BY product_id, store;
/*
store1, store2, store3에 대해서 각각 새 테이블을 만들고
UNION으로 합친다.
프로그래머스에선 보지 못한 방식이라 참신함.
*/