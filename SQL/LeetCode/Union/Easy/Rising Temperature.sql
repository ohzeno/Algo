-- https://leetcode.com/problems/rising-temperature/description/?envType=study-plan&id=sql-i
Create table If Not Exists Weather (id int, recordDate date, temperature int);
Truncate table Weather;
insert into Weather (id, recordDate, temperature)
values ('1', '2015-01-01', '10'),
       ('2', '2015-01-02', '25'),
       ('3', '2015-01-03', '20'),
       ('4', '2015-01-04', '30');
/*
Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
Return the result table in any order.
*/
SELECT w1.id
FROM Weather AS w1, Weather AS w2
WHERE w1.temperature > w2.temperature
  AND DATEDIFF(w1.recordDate, w2.recordDate) = 1;  # DATEDIFF(단위=day, 날짜1, 날짜2) : 날짜1 - 날짜2
  # 고로 위 쿼리는 W1의 이전 날을 가져온다. 다음날이면 -1임.
