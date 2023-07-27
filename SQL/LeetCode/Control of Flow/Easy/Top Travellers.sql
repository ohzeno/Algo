-- https://leetcode.com/problems/top-travellers/?envType=study-plan&id=sql-i
Create Table If Not Exists Users (id int, name varchar(30));
Create Table If Not Exists Rides (id int, user_id int, distance int);
Truncate table Users;
insert into Users (id, name)
values ('1', 'Alice'),
       ('2', 'Bob'),
       ('3', 'Alex'),
       ('4', 'Donald'),
       ('7', 'Lee'),
       ('13', 'Jonathan'),
       ('19', 'Elvis');
Truncate table Rides;
insert into Rides (id, user_id, distance)
values ('1', '1', '120'),
       ('2', '2', '317'),
       ('3', '3', '222'),
       ('4', '7', '100'),
       ('5', '13', '312'),
       ('6', '19', '50'),
       ('7', '7', '120'),
       ('8', '19', '400'),
       ('9', '7', '230');
/*
Write an SQL query to report the distance traveled by each user.
Return the result table ordered by travelled_distance in descending order,
if two or more users traveled the same distance, order them by their name in ascending order.
*/
SELECT U.name, IFNULL(SUM(R.distance), 0) AS travelled_distance
FROM Users AS U
LEFT JOIN Rides AS R
       ON U.id = R.user_id
GROUP BY U.id, U.name  # U.name을 넣지 않으면 sql_mode=only_full_group_by 관련 에러 발생. 주석 참고
ORDER BY travelled_distance DESC, U.name ASC;
/*
LeetCode Easy.
LeetCode에서는 GROUP BY U.id만 해도 된다.
MySQL 5.7 이상 버전에서는 only_full_group_by가 기본적으로 활성화 되어 있다.
이 모드는 SELECT 절에 나열된 모든 컬럼이
GROUP BY 절에 명시되어 있거나
집계 함수에 포함되어 있어야 하는 엄격한 검사를 요구한다.
그렇다고 U.name으로 그룹화하면 이름 중복이 있기에 U.name을 GROUP BY에 넣어줬다.
*/