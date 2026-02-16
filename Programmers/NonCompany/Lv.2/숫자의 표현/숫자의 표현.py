# https://school.programmers.co.kr/learn/courses/30/lessons/12924?language=python3
"""
constraints:
  • n은 10,000 이하의 자연수 입니다.
"""


def solution(n):
    cnt = 0
    m = 1
    while True:
        val = 2 * n / m - m + 1
        if val < 2:
            break
        if not val % 2:
            cnt += 1
        m += 1
    return cnt


inputdatas = [
    {"data": [15], "answer": 4}
]


"""
연습문제
Lv.2. 현 시점 완료한 사람 36,295명, 정답률 76%
베스트 풀이는 수학 공식을 이용했다. 풀이자 중 99% 이상이 공식 증명을 할 줄 모를 것 같다...
공식 증명을 직접하려니 꽤 까다로워서 풀이들을 봤지만
다 복붙 뿐인지 식과 시작점 사이에 과정을 억지로 끼워맞춰서 논리적 흐름이 맞지 않았다.
예를 들어 직관적인 증명은 1, 2, 3...10이라면 블로그 증명들은 1, 2, 7, 10 이런식이라 억지다.
논리적으로 각 명제는 옳지만 명제 사이의 논리적 인과가 전혀 보이지 않는다.

그래서 난 직관적인 등차수열 공식(d가 1인)만 사용해보기로 했다.
등차수열 공식도 수험생 때나 기억하던 것이니 증명부터 해봤다.
a부터 1씩 증가하는 m개의 연속 항의 합 S
S = a + (a+1) + (a+2) + ... + (a+m-1)
S = (a+m-1) + (a+m-2) + ... + (a+1) + a
두 식을 더하면
2S = (2a+m-1) * m
S = m(2a+m-1) / 2
이 S가 n과 같은 a, m의 조합 수를 구해야 한다.
m(2a+m-1) = 2n
m은 항이 둘이라 정리하기 힘드니 편하게 a에 대해서 정리해보자
2a+m-1 = 2n/m
2a = 2n/m - m + 1
a = (2n/m - m + 1) / 2
a는 자연수이므로 2n/m - m + 1 >= 2, 2n/m-m+1이 2로 나누어 떨어져야 한다.
2n/m-m+1이 2보다 작을 경우:
m은 분모, 마이너스 항이라 m이 커져도 조건은 계속 충족되지 않으니 break해주면 된다.
"""

for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
