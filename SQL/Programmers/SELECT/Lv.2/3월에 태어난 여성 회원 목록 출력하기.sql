-- https://school.programmers.co.kr/learn/courses/30/lessons/131120
/*
MEMBER_PROFILE 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성해주세요.
이때 전화번호가 NULL인 경우는 출력대상에서 제외시켜 주시고, 결과는 회원ID를 기준으로 오름차순 정렬해주세요.
*/
SELECT MEMBER_ID, MEMBER_NAME, GENDER,
#        LEFT(DATE_OF_BIRTH, 10) AS DATE_OF_BIRTH  # 왼쪽부터 10글자 가져옴
        DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
# WHERE SUBSTRING(DATE_OF_BIRTH, 6, 2) = 03  # 6번째 글자를 포함한 2글자를 가져옴. 03은 따옴표 안써도 됨.
WHERE DATE_FORMAT(DATE_OF_BIRTH, '%m') = 03
  AND GENDER = 'W'
  AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC;
/*
DATE_FORMAT을 몰랐어서 LEFT, SUBSTRING을 사용했었다.
*/