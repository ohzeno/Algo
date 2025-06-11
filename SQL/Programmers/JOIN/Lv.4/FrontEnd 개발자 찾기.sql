# https://school.programmers.co.kr/learn/courses/30/lessons/276035
/*
SKILLCODES
    NAME	TYPE	UNIQUE	NULLABLE
    NAME	VARCHAR(N)	Y	N
    CATEGORY	VARCHAR(N)	N	N
    CODE	INTEGER	Y	N
DEVELOPERS
    ID	VARCHAR(N)	Y	N
    FIRST_NAME	VARCHAR(N)	N	Y
    LAST_NAME	VARCHAR(N)	N	Y
    EMAIL	VARCHAR(N)	Y	N
    SKILL_CODE	INTEGER	N	N
*/


WITH FRONTEND AS (SELECT CODE
                  FROM SKILLCODES
                  WHERE CATEGORY = 'Front End')
-- (ID, EMAIL, FIRST_NAME, LAST_NAME) 조합 자체에 DISTINCT 적용된다.
SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS AS D
         INNER JOIN FRONTEND AS F
                    ON D.SKILL_CODE & F.CODE > 0
ORDER BY D.ID;


/*
JOIN
Lv.4. 현 시점 완료한 사람 4,166명, 정답률 51%
비트연산 설명 더럽다.
'SKILL_CODE 컬럼은 INTEGER 타입이고, 2진수로 표현했을 때 각 bit는 SKILLCODES 테이블의 코드를 의미합니다. 예를 들어 어떤 개발자의 SKILL_CODE가 400 (=b'110010000')이라면, 이는 SKILLCODES 테이블에서 CODE가 256 (=b'100000000'), 128 (=b'10000000'), 16 (=b'10000') 에 해당하는 스킬을 가졌다는 것을 의미합니다.'

S.CODE를 이진수로 변환, D.SKILL_CODE도 이진수로 변환해서 AND연산 하라는 얘기.
D.SKILL_CODE를 보면
110010000
이게 S.CODE의
100000000
 10000000
    10000
를 보유했다는 말.
거기다 그냥 쿼리 날리면 틀리는데, 여러 스킬을 갖고있으면 여러 행이 생기기 때문에
DISTINCT로 중복 제거해야 한다.
*/
