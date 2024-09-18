# https://school.programmers.co.kr/learn/courses/30/lessons/151136
/*
자동차 종류가 'SUV'인 자동차들의 평균 일일 대여 요금을 출력하는 SQL문을 작성해주세요.
이때 평균 일일 대여 요금은 소수 첫 번째 자리에서 반올림하고, 컬럼명은 AVERAGE_FEE 로 지정해주세요.
CAR_ID: 자동차 ID
CAR_TYPE: 자동차 종류
DAILY_FEE: 일일 대여 요금
OPTIONS: 자동차 옵션 리스트
*/

SELECT ROUND(AVG(DAILY_FEE), 0) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'


/*
SELECT
Lv. 1. 현 시점 완료한 사람 27,693명, 정답률 83%
*/