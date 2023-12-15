-- https://leetcode.com/problems/tree-node/description/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Tree;
Create table Tree (id int, p_id int);
insert into Tree (id, p_id)
values ('1', 'None'),
       ('2', '1'),
       ('3', '1'),
       ('4', '2'),
       ('5', '2');
/*
Each node in the tree can be one of three types:
       "Leaf": if the node is a leaf node.
       "Root": if the node is the root of the tree.
       "Inner": If the node is neither a leaf node nor a root node.
Write an SQL query to report the type of each node in the tree.
Return the result table in any order.
*/
SELECT id,
       CASE
           WHEN p_id IS NULL THEN 'Root'  # 부모가 없음: 루트
           WHEN id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'  # 루트가 아니면서 본인이 부모임: 이너
           ELSE 'Leaf'  # 둘 다 아니면 리프만 남음
       END AS type
FROM Tree
ORDER BY id;