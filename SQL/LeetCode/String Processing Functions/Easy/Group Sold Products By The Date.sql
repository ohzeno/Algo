-- https://leetcode.com/problems/group-sold-products-by-the-date/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Activities;
Create table Activities (sell_date date, product varchar(20));
insert into Activities (sell_date, product)
values ('2020-05-30', 'Headphone'),
       ('2020-06-01', 'Pencil'),
       ('2020-06-02', 'Mask'),
       ('2020-05-30', 'Basketball'),
       ('2020-06-01', 'Bible'),
       ('2020-06-02', 'Mask'),
       ('2020-05-30', 'T-Shirt');
/*
Write an SQL query to find for each date the number of different products sold and their names.
The sold products names for each date should be sorted lexicographically.
Return the result table ordered by sell_date.
*/
SELECT sell_date, COUNT(DISTINCT product) AS num_sold,  # 판매된 제품 종류 수
       GROUP_CONCAT(DISTINCT product ORDER BY product ASC) AS products  # 판매된 제품 종류 목록
FROM Activities
GROUP BY sell_date
