-- https://leetcode.com/problems/calculate-special-bonus/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Employees;
CREATE TABLE Employees (
    employee_id int(4) NOT NULL PRIMARY KEY,
    name varchar(255),
    salary int(4)
);
INSERT INTO Employees (employee_id, name, salary)
VALUES (2, 'Meir', 3000),
       (3, 'Michael', 3800),
       (7, 'Addilyn', 7400),
       (8, 'Juan', 6100),
       (9, 'Kannon', 7700);
/*
Write an SQL query to calculate the bonus of each employee.
The bonus of an employee is 100% of their salary
    if the ID of the employee is an odd number and
    the employee name does not start with the character 'M'.
    The bonus of an employee is 0 otherwise.
Return the result table ordered by employee_id.
*/
SELECT
    employee_id,
    IF(employee_id % 2 = 1 AND name NOT LIKE 'M%', salary, 0) AS bonus  -- IF(condition, true, false)
FROM Employees
ORDER BY employee_id;