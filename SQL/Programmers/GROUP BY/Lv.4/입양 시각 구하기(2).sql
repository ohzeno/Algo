-- https://school.programmers.co.kr/learn/courses/30/lessons/59413
/*
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다.
0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
이때 결과는 시간대 순으로 정렬해야 합니다.
*/
# SET @HOUR := -1; # 변수 설정
# SELECT (@HOUR := @HOUR + 1)           AS HOUR, # 먼저 더하고 출력된다.
#        (SELECT COUNT(*)
#         FROM ANIMAL_OUTS
#         WHERE HOUR(DATETIME) = @HOUR) AS COUNT
# FROM ANIMAL_OUTS
# WHERE @HOUR < 23 # 23 이전일 때만 실행되므로 22 + 1 = 23시까지 출력된다.
# ORDER BY HOUR;
/*
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
ORDER BY HOUR
이 풀이의 경우, 테이블에 hour가 없으면 시간대가 표시되지 않는다.
*/
# RECURSIVE는 자기 자신을 참조할 수 있는 쿼리를 작성할 수 있게 해준다.
WITH RECURSIVE TIME_HOURS AS (SELECT 0 AS HOUR # 베이스 케이스 설정
                                     # 결과 집합을 하나로 합친다.
                              UNION ALL
                              SELECT HOUR + 1
                              FROM TIME_HOURS
                              WHERE HOUR < 23)
SELECT TIME_HOURS.HOUR,
       COUNT(ANIMAL_OUTS.DATETIME) AS COUNT
FROM TIME_HOURS
         LEFT JOIN ANIMAL_OUTS
                   ON HOUR(ANIMAL_OUTS.DATETIME) = TIME_HOURS.HOUR
GROUP BY TIME_HOURS.HOUR
ORDER BY TIME_HOURS.HOUR;

/*
기존 풀이는 HOUR 각각에 대해 ANIMAL_OUTS에 대한 SELECT가 매번 실행됐다.
이번 풀이는 RECURSIVE로 미리 시간을 만든 후 LEFT JOIN으로 합치므로 훨씬 효율적이다.
기존 풀이의 중복 SELECT 내에서 COUNT를 하는 부분도
이번 풀이에서 GROUP BY를 통해 효율화 되었다.
*/