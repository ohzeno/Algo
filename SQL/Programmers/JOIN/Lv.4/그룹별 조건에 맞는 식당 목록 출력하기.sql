-- https://school.programmers.co.kr/learn/courses/30/lessons/131124
/*
MEMBER_PROFILE와 REST_REVIEW 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성해주세요.
회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 작성해주시고,
결과는 리뷰 작성일을 기준으로 오름차순,
리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬해주세요.
*/
# 리뷰를 가장 많이 작성한 회원
WITH MAX_REV_MEMBER AS (SELECT MEMBER_ID, COUNT(*) AS REVIEW_CNT
                        FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                        ORDER BY REVIEW_CNT DESC
                        LIMIT 1),
    # 그 회원이 작성한 리뷰들
     REVIEWS AS (SELECT REV.MEMBER_ID, REV.REVIEW_TEXT, REV.REVIEW_DATE
                 FROM MAX_REV_MEMBER AS MEM
                          JOIN REST_REVIEW AS REV
                               ON MEM.MEMBER_ID = REV.MEMBER_ID)
SELECT PRO.MEMBER_NAME,
       REV.REVIEW_TEXT,
       DATE_FORMAT(REV.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS PRO
         JOIN REVIEWS AS REV # 이름 가져와서 합쳐줌.
              ON PRO.MEMBER_ID = REV.MEMBER_ID
ORDER BY REV.REVIEW_DATE, REV.REVIEW_TEXT


/*
WITH를 사용하지 않고 해보려다가 서브쿼리가 너무 복잡해서 그냥 WITH를 사용했다.
이전과는 명칭들만 조금씩 달라졌다.
리뷰를 가장 많이 작성한 회원이 여럿이 나오긴 하는데,
문제에서 '회원들'이 아니라 '회원'이라고 해서 LIMIT을 사용했다.
*/
