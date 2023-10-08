-- https://leetcode.com/problems/game-play-analysis-i/?envType=study-plan&id=sql-i
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played)
values ('1', '2', '2016-03-01', '5'),
       ('1', '2', '2016-05-02', '6'),
       ('2', '3', '2017-06-25', '1'),
       ('3', '1', '2016-03-02', '0'),
       ('3', '4', '2018-07-03', '5');
/*
Write an SQL query to report the first login date for each player.
Return the result table in any order.
*/
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
