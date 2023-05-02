-- https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS World;


/*
Create table If Not Exists Users
Truncate table Users
insert into Users
리트코드의 스키마는 위와 같은 과정을 거친다.
하지만 이렇게 하면 이미 Users 테이블이 존재할 경우 데이터만 제거된다.
그리고 새로 입력하려던 Users와 기존 Users의 스키마가 다를 경우 오류가 발생한다.
그래서 DROP TABLE IF EXISTS Users; 를 사용하여 기존 테이블이 존재할 경우 제거하고
새로운 테이블을 생성하는게 좋다.
*/