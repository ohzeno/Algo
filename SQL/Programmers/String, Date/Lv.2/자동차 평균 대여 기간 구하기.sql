# https://school.programmers.co.kr/learn/courses/30/lessons/157342
/*
CAR_RENTAL_COMPANY_RENTAL_HISTORY
    Column name	Type	Nullable
    HISTORY_ID	INTEGER	FALSE
    CAR_ID	INTEGER	FALSE
    START_DATE	DATE	FALSE
    END_DATE	DATE	FALSE
*/


-- 코드를 입력하세요
WITH RENTAL_HISTORY AS (
    SELECT CAR_ID,
           AVG(DATEDIFF(END_DATE, START_DATE) + 1) AS AVG_RENTAL_DAYS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    GROUP BY CAR_ID
    HAVING AVG_RENTAL_DAYS >= 7
)
SELECT CAR_ID,
       ROUND(AVG_RENTAL_DAYS, 1) AS AVERAGE_DURATION
FROM RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;


/*
String, Date
Lv.2. 현 시점 완료한 사람 16,616명, 정답률 78%
DATEDIFF는 두 날짜의 차이를 일수로 반환한다. 종료일 포함하려면 + 1을 해줘야 한다.
WHERE는 그룹화 이전에 작동해서 SELECT절에서 사용한 칼럼명을 인식하지 못함
HAVING은 그룹화 이후에 작동하므로 그룹화된 칼럼명을 인식할 수 있다.
Lv.4보다 헤맸다.
*/
