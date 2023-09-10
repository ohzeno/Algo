-- https://leetcode.com/problems/daily-leads-and-partners/description/?envType=study-plan&id=sql-i
Create table If Not Exists DailySales(date_id date, make_name varchar(20), lead_id int, partner_id int);
Truncate table DailySales;
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-8', 'toyota', '0', '1'),
       ('2020-12-8', 'toyota', '1', '0'),
       ('2020-12-8', 'toyota', '1', '2'),
       ('2020-12-7', 'toyota', '0', '2'),
       ('2020-12-7', 'toyota', '0', '1'),
       ('2020-12-8', 'honda', '1', '2'),
       ('2020-12-8', 'honda', '2', '1'),
       ('2020-12-7', 'honda', '0', '1'),
       ('2020-12-7', 'honda', '1', '2'),
       ('2020-12-7', 'honda', '2', '1');
/*
Write an SQL query that will, for each date_id and make_name,
return the number of distinct lead_id's and distinct partner_id's.
Return the result table in any order.
*/
SELECT date_id, make_name,
       COUNT(DISTINCT lead_id) AS unique_leads,
       COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name
