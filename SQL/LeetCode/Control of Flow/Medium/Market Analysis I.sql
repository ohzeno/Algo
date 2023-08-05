-- https://leetcode.com/problems/market-analysis-i/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Items;
Create table Users (user_id int, join_date date, favorite_brand varchar(10));
Create table Orders (order_id int, order_date date, item_id int, buyer_id int, seller_id int);
Create table Items (item_id int, item_brand varchar(10));
insert into Users (user_id, join_date, favorite_brand)
values ('1', '2018-01-01', 'Lenovo'),
       ('2', '2018-02-09', 'Samsung'),
       ('3', '2018-01-19', 'LG'),
       ('4', '2018-05-21', 'HP');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id)
values ('1', '2019-08-01', '4', '1', '2'),
       ('2', '2018-08-02', '2', '1', '3'),
       ('3', '2019-08-03', '3', '2', '3'),
       ('4', '2018-08-04', '1', '4', '2'),
       ('5', '2018-08-04', '1', '3', '4'),
       ('6', '2019-08-05', '2', '2', '4');
insert into Items (item_id, item_brand)
values ('1', 'Samsung'),
       ('2', 'Lenovo'),
       ('3', 'LG'),
       ('4', 'HP');
/*
Write an SQL query to find for each user,
the join date and the number of orders they made as a buyer in 2019.
Return the result table in any order.
*/
SELECT U.user_id AS buyer_id,
       U.join_date,
       COUNT(O.order_id) AS orders_in_2019  # count에서 0이 나올것이라 ifnull 필요없음.
FROM Users AS U
LEFT JOIN Orders AS O
       ON U.user_id = O.buyer_id AND
          YEAR(O.order_date) = 2019
GROUP BY U.user_id, U.join_date  # u.join_date가 select절에 있으므로 group by에도 있어야 한다. 다행히, join_date는 user_id당 한개다.
/*
LeetCode Medium.
초기안은 이랬다. Join까지는 19년에 주문하지 않은 사람도 테이블에 포함되지만
where절에서 19년에 주문하지 않은 사람은 레코드 자체가 제거된다.
ifnull은 left join값이 null인 것에 적용되어야 하는데
where때문에 레코드 자체가 제거되어 18년에 주문하지 않은 사람은 결과에 나타나지 않았다.
그래서 join on에서 year를 적용해서 18년에 주문하지 않은 사람의 레코드가 남아있도록 했다.
SELECT U.user_id AS buyer_id,
       U.join_date,
       IFNULL(COUNT(O.order_id), 0) AS orders_in_2019
FROM Users AS U
LEFT JOIN Orders AS O
       ON U.user_id = O.buyer_id
WHERE YEAR(O.order_date) = 2019
GROUP BY U.user_id
*/