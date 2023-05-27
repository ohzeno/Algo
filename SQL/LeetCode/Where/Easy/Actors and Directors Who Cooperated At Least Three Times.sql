-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS ActorDirector;
Create table ActorDirector (actor_id int, director_id int, timestamp int);
insert into ActorDirector (actor_id, director_id, timestamp)
values ('1', '1', '0'),
       ('1', '1', '1'),
       ('1', '1', '2'),
       ('1', '2', '3'),
       ('1', '2', '4'),
       ('2', '1', '5'),
       ('2', '1', '6');
/*
Write a SQL query for a report that provides the pairs (actor_id, director_id)
where the actor has cooperated with the director at least three times.
Return the result table in any order.
*/
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id  # 배우마다 감독이랑 몇번 협업했는지 구하는것보다 처음부터 묶는게 편함
HAVING COUNT(*) >= 3;