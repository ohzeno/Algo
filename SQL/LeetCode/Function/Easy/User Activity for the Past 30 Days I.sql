-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/?envType=study-plan&id=sql-i
Create table If Not Exists Activity (
    user_id int, session_id int, activity_date date,
    activity_type ENUM('open_session', 'end_session', 'scroll_down', 'send_message')
);
Truncate table Activity;
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('1', '1', '2019-07-20', 'open_session'),
       ('1', '1', '2019-07-20', 'scroll_down'),
       ('1', '1', '2019-07-20', 'end_session'),
       ('2', '4', '2019-07-20', 'open_session'),
       ('2', '4', '2019-07-21', 'send_message'),
       ('2', '4', '2019-07-21', 'end_session'),
       ('3', '2', '2019-07-21', 'open_session'),
       ('3', '2', '2019-07-21', 'send_message'),
       ('3', '2', '2019-07-21', 'end_session'),
       ('4', '3', '2019-06-25', 'open_session'),
       ('4', '3', '2019-06-25', 'end_session');
/*
Write an SQL query to find the
daily active user count for a period of 30 days ending 2019-07-27 inclusively.
A user was active on someday if they made at least one activity on that day.
Return the result table in any order.
*/
SELECT activity_date AS day,
       COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date
    BETWEEN '2019-07-27' - INTERVAL 29 DAY  # DATE_SUB('2019-07-27', INTERVAL 29 DAY)이나 DATE_ADD('2019-07-27', INTERVAL -29 DAY)도 가능
        AND '2019-07-27'
GROUP BY activity_date
