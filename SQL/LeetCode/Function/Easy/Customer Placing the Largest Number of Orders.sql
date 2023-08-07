-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/?envType=study-plan&id=sql-i
Create table If Not Exists orders (order_number int, customer_number int);
Truncate table orders;
insert into orders (order_number, customer_number)
values ('1', '1'),
       ('2', '2'),
       ('3', '3'),
       ('4', '3');
/*
Write an SQL query to find the
customer_number for the customer who has placed the largest number of orders.
The test cases are generated so that exactly one customer will have placed more orders than any other customer.
*/
SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC  # 고객으로 그룹화하고, 주문수를 내림차순으로 정렬
LIMIT 1;  # 한 명만 더 많도록 테스트 케이스가 생성된다고 했으니, 1개만 출력하면 된다.
