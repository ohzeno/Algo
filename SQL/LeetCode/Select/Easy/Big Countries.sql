-- https://leetcode.com/problems/big-countries/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS World;
CREATE TABLE World (
    name VARCHAR(50) NOT NULL PRIMARY KEY,
    continent VARCHAR(50),
    area INT,
    population INT,
    gdp INT
);
INSERT INTO World (name, continent, area, population, gdp)
VALUES ('Afghanistan', 'Asia', 652230, 25500100, 20343000),
       ('Albania', 'Europe', 28748, 2831741, 12960000),
       ('Algeria', 'Africa', 2381741, 37100000, 188681000),
       ('Andorra', 'Europe', 468, 78115, 3712000),
       ('Angola', 'Africa', 1246700, 20609294, 100990000);
/*-- A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write an SQL query to report the name, population, and area of the big countries.

Return the result table in any order.

The query result format is in the following example.*/
SELECT name, population, area FROM World
WHERE area >= 3000000 OR population >= 25000000;