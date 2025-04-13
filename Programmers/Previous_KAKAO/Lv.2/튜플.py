# https://school.programmers.co.kr/learn/courses/30/lessons/64065
"""
constraints:

"""


def solution(s):
    """
    n튜플은 n개 원소 가짐
    중복원소 가능
    원소 순서 있음
    중복 없는 n개 원소 가지면 {{a1}, {a1, a2}, ..., {a1, a2, ..., an}} 형태로 표현 가능
    이 형태에서는 원소 순서 바뀌어도 상관없음(2차원 내에서)
    튜플 표현 문자열 주어지면 어떤 튜플인지 배열로 반환
    """
    datas = [set(map(int, x.split(','))) for x in s[2:-2].split('},{')]
    ans = []
    pre = set()
    for data in sorted(datas, key=len):
        ans.append((data - pre).pop())
        pre = data
    return ans


inputdatas = [
    {"data": ["{{2},{2,1},{2,1,3},{2,1,3,4}}"], "answer": [2, 1, 3, 4]},
    {"data": ["{{1,2,3},{2,1},{1,2,4,3},{2}}"], "answer": [2, 1, 3, 4]},
    {"data": ["{{20,111},{111}}"], "answer": [111, 20]},
    {"data": ["{{123}}"], "answer": [123]},
    {"data": ["{{4,2,3},{3},{2,3,4,1},{2,3}}"], "answer": [3, 2, 4, 1]}
]


"""
2019 카카오 개발자 겨울 인턴십
Lv.2. 현 시점 완료한 사람 24,982명, 정답률 65%
이전 풀이와 크게 다른건 없다. 파싱 과정에서 int로 변경, set처리도 한번에 해줬다.
이전엔 한참 헤매서 36분 걸렸었는데 이번엔 개선까지 포함해서 7분 걸렸다.
set 삽입 순서가 유지되니 pre를 따로 두지 않아도 풀 수 있지만, 
자료구조 특성상 오해가 생길 수 있어 pre를 두었다.
3회차. 6분 걸렸다. 로직은 딱히 크게 바뀐게 없어서 코드는 그대로.
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
