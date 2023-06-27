-- https://school.programmers.co.kr/learn/courses/30/lessons/59413
/*
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다.
0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
이때 결과는 시간대 순으로 정렬해야 합니다.
*/
SET @HOUR := -1;  # 변수 설정
SELECT (@HOUR := @HOUR + 1) AS HOUR,  # 먼저 더하고 출력된다.
       (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23  # 23 이전일 때만 실행되므로 22 + 1 = 23시까지 출력된다.
/*
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
ORDER BY HOUR
이 풀이의 경우, 테이블에 hour가 없으면 시간대가 표시되지 않는다.
*/