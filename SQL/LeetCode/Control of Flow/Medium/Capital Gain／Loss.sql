-- https://leetcode.com/problems/capital-gainloss/?envType=study-plan&id=sql-i
Create Table If Not Exists Stocks (stock_name varchar(15), operation ENUM('Sell', 'Buy'), operation_day int, price int);
Truncate table Stocks;
insert into Stocks (stock_name, operation, operation_day, price)
values ('Leetcode', 'Buy', '1', '1000'),
       ('Corona Masks', 'Buy', '2', '10'),
       ('Leetcode', 'Sell', '5', '9000'),
       ('Handbags', 'Buy', '17', '30000'),
       ('Corona Masks', 'Sell', '3', '1010'),
       ('Corona Masks', 'Buy', '4', '1000'),
       ('Corona Masks', 'Sell', '5', '500'),
       ('Corona Masks', 'Buy', '6', '1000'),
       ('Handbags', 'Sell', '29', '7000'),
       ('Corona Masks', 'Sell', '10', '10000');
/*
Write an SQL query to report the Capital gain/loss for each stock.
The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.
Return the result table in any order.
(stock_name, operation_day) is the primary key for this table.
The operation column is an ENUM of type ('Sell', 'Buy')
각 매수와 매도는 한 쌍으로 나타남이 보장된다.
*/
SELECT stock_name,
       SUM(IF(operation = 'Buy', -price, price)) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
/*
LeetCode Medium.
각각의 수익을 더해야 하는데, 매 쌍마다 매도-매수 가격이 수익이다.
결국 그걸 다 더한건 매도 합 - 매수 합과 같다
*/