-- https://leetcode.com/problems/second-highest-salary/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Employee;
Create table Employee (id int, salary int);
insert into Employee (id, salary)
values ('1', '100'),
       ('2', '200'),
       ('3', '300');
/*
Write an SQL query to report the second highest salary from the Employee table.
If there is no second highest salary, the query should report null.
*/
SELECT MAX(FROM_SECOND.salary) AS SecondHighestSalary  # 그 중에서 최고값을 가져온다. MAX는 값이 없으면 NULL을 반환함.
FROM (
    SELECT salary
    FROM Employee
    WHERE salary < (SELECT MAX(salary) FROM Employee)  # 최고값보다 작은 값만 가져온 테이블
) AS FROM_SECOND;  # 파생 테이블에는 별칭이 필요하다.

SELECT IFNULL(  # IFNULL은 첫번째 인자가 NULL이 아니면 첫번째 인자를, NULL이면 두번째 인자를 반환한다.
    (SELECT DISTINCT salary AS SecondHighestSalary  # 안쪽 쿼리만 실행하면 2등이 없을 때 NULL이 반환되지 않고 빈 테이블이 반환된다.
     FROM Employee
     ORDER BY salary DESC
     LIMIT 1 OFFSET 1),  # OFFSET은 몇 행을 건너뛸지 지정한다. LIMIT과 같이 쓰인다.
    NULL) AS SecondHighestSalary;  # IFNULL이 값을 반환하기 때문에 FROM 절이 필요없다.

SELECT MAX(salary) AS SecondHighestSalary  # 2등부터 가져온 테이블에서 최고값을 가져온다.
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);  # WHERE 제약이 먼저 적용되어 2등부터 가져온 테이블에 MAX가 적용된다.
/*
다른 답안들이 직관적이지 않아서 내 풀이를 포함해 다 적어놨다.
*/