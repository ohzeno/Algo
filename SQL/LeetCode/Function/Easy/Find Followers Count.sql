-- https://leetcode.com/problems/find-followers-count/?envType=study-plan&id=sql-i
Create table If Not Exists Followers(user_id int, follower_id int);
Truncate table Followers;
insert into Followers (user_id, follower_id)
values ('0', '1'),
       ('1', '0'),
       ('2', '0'),
       ('2', '1');
/*
Write an SQL query that will, for each user, return the number of followers.
Return the result table ordered by user_id in ascending order.
(user_id, follower_id) is the primary key for this table.
*/
SELECT user_id, COUNT(follower_id) AS followers_count  # (user_id, follower_id)가 primary key이므로 dictinct 필요 없음
FROM Followers
GROUP BY user_id
ORDER BY user_id;
