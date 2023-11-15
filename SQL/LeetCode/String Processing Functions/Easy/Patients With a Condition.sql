-- https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan&id=sql-i
DROP TABLE IF EXISTS Patients;
Create table Patients (patient_id int, patient_name varchar(30), conditions varchar(100));
insert into Patients (patient_id, patient_name, conditions)
values ('1', 'Daniel', 'YFEV COUGH'),
       ('2', 'Alice', ''),
       ('3', 'Bob', 'DIAB100 MYOP'),
       ('4', 'George', 'ACNE DIAB100'),
       ('5', 'Alain', 'DIAB201');
/*
Write an SQL query to report the
patient_id, patient_name and conditions of the patients who have Type I Diabetes.
Type I Diabetes always starts with DIAB1 prefix.
Return the result table in any order.
*/
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE '% DIAB1%'  # DIAB1 진단이 첫 단어가 아닐 경우
   OR conditions LIKE 'DIAB1%';  # 첫 단어일 경우