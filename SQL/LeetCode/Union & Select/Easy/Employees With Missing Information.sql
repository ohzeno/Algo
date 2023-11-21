-- https://leetcode.com/problems/employees-with-missing-information/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Salaries;
Create table Employees (employee_id int, name varchar(30));
insert into Employees (employee_id, name)
values ('2', 'Crew'),
       ('4', 'Haven'),
       ('5', 'Kristian');
Create table Salaries (employee_id int, salary int);
insert into Salaries (employee_id, salary)
values ('5', '76071'),
       ('1', '22517'),
       ('4', '63539');
/*
Write an SQL query to report the
IDs of all the employees with missing information.
The information of an employee is missing if:
       The employee's name is missing, or
       The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.
*/
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)  # 월급 없는 사람
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)  # 이름 없는 사람
ORDER BY employee_id ASC;
