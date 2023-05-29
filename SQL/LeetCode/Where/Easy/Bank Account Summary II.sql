-- https://leetcode.com/problems/bank-account-summary-ii/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Transactions;
Create table Users (account int, name varchar(20));
Create table Transactions (trans_id int, account int, amount int, transacted_on date);
insert into Users (account, name)
values ('900001', 'Alice'),
       ('900002', 'Bob'),
       ('900003', 'Charlie');
insert into Transactions (trans_id, account, amount, transacted_on)
values ('1', '900001', '7000', '2020-08-01'),
       ('2', '900001', '7000', '2020-09-01'),
       ('3', '900001', '-3000', '2020-09-02'),
       ('4', '900002', '1000', '2020-09-12'),
       ('5', '900003', '6000', '2020-08-07'),
       ('6', '900003', '6000', '2020-09-07'),
       ('7', '900003', '-4000', '2020-09-11');
/*
Write an SQL query to report the name and balance of users with a balance higher than 10000.
The balance of an account is equal to the sum of the amounts of all transactions involving that account.
Return the result table in any order.
*/
SELECT U.name, SUM(T.amount) AS balance
FROM Users AS U
JOIN Transactions AS T
       ON U.account = T.account
GROUP BY U.account
HAVING balance > 10000;