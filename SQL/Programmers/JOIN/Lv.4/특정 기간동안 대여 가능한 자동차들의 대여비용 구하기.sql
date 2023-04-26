-- https://school.programmers.co.kr/learn/courses/30/lessons/157339
/*
CAR_RENTAL_COMPANY_CAR 테이블과
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과
CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서
자동차 종류가 '세단' 또는 'SUV' 인 자동차 중
2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고
30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서
자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요.
결과는 대여 금액을 기준으로 내림차순 정렬하고,
대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬,
자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.
*/
WITH AVAILABE_CARS AS (
    SELECT CAR_ID, CAR_TYPE, DAILY_FEE AS FEE
    FROM CAR_RENTAL_COMPANY_CAR AS CAR
    WHERE CAR_TYPE IN ('세단', 'SUV')  # 종류가 세단, SUV
      AND CAR_ID NOT IN (  # 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE BETWEEN '2022-11-01' AND '2022-11-30'  # 시작일이 11월 1일부터 11월 30일 사이
           OR END_DATE BETWEEN '2022-11-01' AND '2022-11-30'  # 종료일이 11월 1일부터 11월 30일 사이
           OR '2022-11-01' BETWEEN START_DATE AND END_DATE  # 예를 들어 10.01~12.01인 경우 위 조건을 만족해도 대여 불가
      )
), DISCOUNTED_FEES AS (
    SELECT
        AC.CAR_ID, AC.CAR_TYPE,
        AC.FEE * (100 - DP.DISCOUNT_RATE)/100 * 30 AS FEE  # 할인한 가격으로 30일 대여비용
    FROM AVAILABE_CARS AS AC
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS DP
        ON AC.CAR_TYPE = DP.CAR_TYPE
               AND DP.DURATION_TYPE = '30일 이상'  # 30일 대여할 거라서 이것만
)
SELECT CAR_ID, CAR_TYPE, CAST(FEE AS SIGNED INT) AS FEE  # 그냥 INT하면 오류남. 부호 있는 정수로 캐스팅.
FROM DISCOUNTED_FEES
WHERE FEE BETWEEN 500000 AND 1999999  # BETWEEN은 []임. 양끝 포함.
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC
