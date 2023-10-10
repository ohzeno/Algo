-- https://leetcode.com/problems/find-customer-referee/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Customer;
CREATE TABLE Customer (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30),
    referee_id INT
);
INSERT INTO Customer (id, name, referee_id)
VALUES ('1', 'Will', null),
       ('2', 'Jane', null),
       ('3', 'Alex', '2'),
       ('4', 'Bill', null),
       ('5', 'Zack', '1'),
       ('6', 'Mark', '2');
/*Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
Return the result table in any order.
The query result format is in the following example.*/
SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS NULL;