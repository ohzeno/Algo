-- https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Products;
CREATE TABLE Products (
    product_id int NOT NULL PRIMARY KEY,
    low_fats varchar(255),
    recyclable varchar(255)
);
INSERT INTO Products (product_id, low_fats, recyclable)
VALUES ('0', 'Y', 'N'),
       ('1', 'Y', 'Y'),
       ('2', 'N', 'Y'),
       ('3', 'Y', 'Y'),
       ('4', 'N', 'N');
/*product_id is the primary key for this table.
low_fats is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

Write an SQL query to find the ids of products that are both low fat and recyclable.
Return the result table in any order.*/
SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y';