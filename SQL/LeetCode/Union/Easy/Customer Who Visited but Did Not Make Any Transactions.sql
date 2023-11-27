-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/?envType=study-plan&id=sql-i
Create table If Not Exists Visits(visit_id int, customer_id int);
Create table If Not Exists Transactions(transaction_id int, visit_id int, amount int);
Truncate table Visits;
insert into Visits (visit_id, customer_id)
values ('1', '23'),
       ('2', '9'),
       ('4', '30'),
       ('5', '54'),
       ('6', '96'),
       ('7', '54'),
       ('8', '54');
Truncate table Transactions;
insert into Transactions (transaction_id, visit_id, amount)
values ('2', '5', '310'),
       ('3', '5', '300'),
       ('9', '5', '200'),
       ('12', '1', '910'),
       ('13', '2', '970');
/*
Write a SQL query to find
the IDs of the users who visited without making any transactions
and the number of times they made these types of visits.
Return the result table sorted in any order.
*/
SELECT v.customer_id AS customer_id,
       COUNT(v.visit_id) AS count_no_trans
FROM Visits AS v  # visit한 경우이므로 Visits 기반
LEFT JOIN Transactions AS t
       ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL  # transaction이 없는 경우
GROUP BY v.customer_id;  # count를 위해