-- https://leetcode.com/problems/article-views-i/?envType=study-plan&id=sql-i
Create table If Not Exists Views (article_id int, author_id int, viewer_id int, view_date date);
Truncate table Views;
insert into Views (article_id, author_id, viewer_id, view_date)
values ('1', '3', '5', '2019-08-01'),
       ('1', '3', '6', '2019-08-02'),
       ('2', '7', '7', '2019-08-01'),
       ('2', '7', '6', '2019-08-02'),
       ('4', '7', '1', '2019-07-22'),
       ('3', '4', '4', '2019-07-21'),
       ('3', '4', '4', '2019-07-21');
/*
Write an SQL query to find all the authors that viewed at least one of their own articles.
Return the result table sorted by id in ascending order.
*/
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;