-- https://leetcode.com/problems/swap-salary/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Salary;
Create table Salary (id int, name varchar(100), sex char(1), salary int);
insert into Salary (id, name, sex, salary)
values ('1', 'A', 'm', '2500'),
       ('2', 'B', 'f', '1500'),
       ('3', 'C', 'm', '5500'),
       ('4', 'D', 'f', '500');
/*
Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa)
with a single update statement and no intermediate temporary tables.
Note that you must write a single update statement, do not write any select statement for this problem.
*/
UPDATE Salary  -- Salary를 업데이트 하겠다.
SET sex =  -- sex에 할당하겠다.
        CASE sex  -- sex값에 따라 반환할 값이 달라진다.
            WHEN 'f' THEN 'm'  -- sex가 f면 m을 반환
            ELSE 'f'
        END;
