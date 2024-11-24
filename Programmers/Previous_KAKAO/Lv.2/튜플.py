# https://school.programmers.co.kr/learn/courses/30/lessons/64065
"""
constraints:

"""


def solution(s):
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
Lv.2. 현 시점 완료한 사람 23,396명, 정답률 64%
이전 풀이와 크게 다른건 없다. 파싱 과정에서 int로 변경, set처리도 한번에 해줬다.
이전엔 한참 헤매서 36분 걸렸었는데 이번엔 개선까지 포함해서 7분 걸렸다.
set 삽입 순서가 유지되니 pre를 따로 두지 않아도 풀 수 있지만, 
자료구조 특성상 오해가 생길 수 있어 pre를 두었다.
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
