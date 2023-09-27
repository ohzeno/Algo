-- https://leetcode.com/problems/customers-who-never-order/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Orders;
CREATE TABLE Customers (
    Id int NOT NULL PRIMARY KEY,
    Name varchar(255)
);
CREATE TABLE Orders (
    Id int NOT NULL PRIMARY KEY,
    CustomerId int,
    FOREIGN KEY (CustomerId) REFERENCES Customers(Id)
);
INSERT INTO Customers (Id, Name)
VALUES ('1', 'Joe'),
       ('2', 'Henry'),
       ('3', 'Sam'),
       ('4', 'Max');
INSERT INTO Orders (Id, CustomerId)
VALUES ('1', '3'),
       ('2', '1');
-- Write an SQL query to report all customers who never order anything.
-- Return the result table in any order.
SELECT name as Customers FROM Customers
                         WHERE id NOT IN (
                         SELECT DISTINCT CustomerId FROM Orders
                                                    );
-- 자동정렬이 뭔가 이상하다...