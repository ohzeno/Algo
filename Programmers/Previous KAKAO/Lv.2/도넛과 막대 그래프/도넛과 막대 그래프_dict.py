# https://school.programmers.co.kr/learn/courses/30/lessons/17682
"""
도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프들. 이 그래프들은 1개 이상의 정점과, 정점들을 연결하는 단방향 간선으로 이루어짐.

- 크기가 n인 도넛 모양 그래프는 n개 정점과 n개 간선이 있음. 아무 한 정점에서 출발해 이용한 적 없는 간선을 계속 따라가면 나머지 n - 1개의 정점들을 한 번씩 방문한 뒤 원래 출발했던 정점으로 돌아오게 됨. 도넛 모양 그래프의 형태는 다음과 같습니다.

- 크기가 n인 막대 모양 그래프는 n개 정점과 n - 1개 간선이 있음. 임의의 한 정점에서 출발해 간선을 계속 따라가면 나머지 n - 1개의 정점을 한 번씩 방문하게 되는 정점이 단 하나 존재. 막대 모양 그래프의 형태는 다음과 같습니다.

- 크기가 n인 8자 모양 그래프는 2n+1개 정점과 2n+2개 간선이 있음. 8자 모양 그래프는 크기가 동일한 2개의 도넛 모양 그래프에서 정점을 하나씩 골라 결합시킨 형태의 그래프. 8자 모양 그래프의 형태는 다음과 같습니다.

도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프가 여러 개 있음. 이 그래프들과 무관한 정점을 하나 생성한 뒤, 각 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 임의의 정점 하나로 향하는 간선들을 연결했음.

그 후 각 정점에 서로 다른 번호를 매겼습니다.

이때 당신은 그래프의 간선 정보가 주어지면 생성한 정점의 번호, 정점을 생성하기 전 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수를 구해야 합니다.

그래프의 간선 정보를 담은 2차원 정수 배열 edges가 매개변수로 주어집니다. 이때, 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수를 순서대로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

### 제한사항
- 1 ≤ edges의 길이 ≤ 1,000,000
    - edges의 원소는 [a,b] 형태이며, a번 정점에서 b번 정점으로 향하는 간선이 있다는 것을 나타냄
    - 1 ≤ a, b ≤ 1,000,000
- 문제의 조건에 맞는 그래프가 주어집니다.
- 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 수의 합은 2이상입니다.
"""


def solution(edges):
    inout = {}
    for a, b in edges:
        inout.setdefault(a, {"in": 0, "out": 0})["out"] += 1
        inout.setdefault(b, {"in": 0, "out": 0})["in"] += 1
    st = stick = eight = 0
    for node, io in inout.items():
        # 들어오는 길이 없고 나가는 길이 2개 이상이면 새로 생성한 정점
        if not st and not io["in"] and io["out"] > 1:
            st = node
        elif not io["out"]:  # 나가는 길이 없으면 막대 그래프 종점
            stick += 1
        elif io["out"] == 2:  # 나가는 길이 2개면 8자 그래프 중앙.
            eight += 1
    # 도넛 그래프는 총 그래프 수 - 막대 그래프 수 - 8자 그래프 수
    donut = inout[st]["out"] - stick - eight
    return [st, donut, stick, eight]


inputdatas = [
    {"data": [[[2, 3], [4, 3], [1, 1], [2, 1]]], "answer": [2, 1, 1, 0]},
    {"data": [[[2, 4], [4, 3], [1, 1], [2, 1]]], "answer": [2, 1, 1, 0]},
    {"data": [[[2, 4], [4, 3], [5, 1], [2, 1], [1, 5]]], "answer": [2, 1, 1, 0]},
    {"data": [[[2, 4], [4, 3], [5, 1], [2, 5], [1, 5]]], "answer": [2, 1, 1, 0]},
    {
        "data": [[[2, 4], [4, 3], [5, 1], [1, 6], [6, 5], [2, 5]]],
        "answer": [2, 1, 1, 0],
    },
    {
        "data": [[[2, 4], [4, 3], [5, 1], [1, 6], [6, 5], [2, 1]]],
        "answer": [2, 1, 1, 0],
    },
    {
        "data": [[[2, 4], [4, 3], [5, 1], [1, 6], [6, 5], [2, 6]]],
        "answer": [2, 1, 1, 0],
    },
    {
        "data": [[[2, 4], [4, 3], [5, 1], [1, 6], [6, 7], [7, 5], [2, 1]]],
        "answer": [2, 1, 1, 0],
    },
    {
        "data": [[[2, 4], [4, 3], [5, 1], [1, 6], [6, 7], [7, 5], [2, 6]]],
        "answer": [2, 1, 1, 0],
    },
    {
        "data": [[[2, 4], [4, 3], [5, 1], [1, 6], [6, 7], [7, 5], [2, 5]]],
        "answer": [2, 1, 1, 0],
    },
    {
        "data": [[[2, 4], [4, 3], [5, 1], [1, 6], [6, 7], [7, 5], [2, 7]]],
        "answer": [2, 1, 1, 0],
    },
    {
        "data": [
            [
                [4, 11],
                [1, 12],
                [8, 3],
                [12, 7],
                [4, 2],
                [7, 11],
                [4, 8],
                [9, 6],
                [10, 11],
                [6, 10],
                [3, 5],
                [11, 1],
                [5, 3],
                [11, 9],
                [3, 8],
            ]
        ],
        "answer": [4, 0, 1, 2],
    },
    {
        "data": [
            [
                [4, 11],
                [1, 12],
                [8, 3],
                [12, 7],
                [4, 2],
                [7, 11],
                [4, 3],
                [9, 6],
                [10, 11],
                [6, 10],
                [3, 5],
                [11, 1],
                [5, 3],
                [11, 9],
                [3, 8],
            ]
        ],
        "answer": [4, 0, 1, 2],
    },
    {
        "data": [
            [
                [4, 11],
                [1, 12],
                [8, 3],
                [12, 7],
                [4, 2],
                [7, 11],
                [4, 5],
                [9, 6],
                [10, 11],
                [6, 10],
                [3, 5],
                [11, 1],
                [5, 3],
                [11, 9],
                [3, 8],
            ]
        ],
        "answer": [4, 0, 1, 2],
    },
    {
        "data": [
            [
                [4, 7],
                [1, 12],
                [8, 3],
                [12, 7],
                [4, 2],
                [7, 11],
                [4, 5],
                [9, 6],
                [10, 11],
                [6, 10],
                [3, 5],
                [11, 1],
                [5, 3],
                [11, 9],
                [3, 8],
            ]
        ],
        "answer": [4, 0, 1, 2],
    },
    {
        "data": [
            [
                [4, 1],
                [1, 12],
                [8, 3],
                [12, 7],
                [4, 2],
                [7, 11],
                [4, 5],
                [9, 6],
                [10, 11],
                [6, 10],
                [3, 5],
                [11, 1],
                [5, 3],
                [11, 9],
                [3, 8],
            ]
        ],
        "answer": [4, 0, 1, 2],
    },
    {
        "data": [
            [
                [4, 12],
                [1, 12],
                [8, 3],
                [12, 7],
                [4, 2],
                [7, 11],
                [4, 5],
                [9, 6],
                [10, 11],
                [6, 10],
                [3, 5],
                [11, 1],
                [5, 3],
                [11, 9],
                [3, 8],
            ]
        ],
        "answer": [4, 0, 1, 2],
    },
]

"""
2024 KAKAO WINTER INTERNSHIP 기출
Lv.2. 현 시점 완료한 사람 1704명, 정답률 21%
올라온지 얼마 안됐지만 푼 사람은 많고 기존 문제들에 비해 레벨은 낮은데 정답률은 낮은걸 보니
기존 문제들은 그냥 블로그 풀이 복붙으로 푼 사람이 엄청나게 많은 듯 하다.
코테 당시에는 dfs로 풀었다.
진입 진출 차수만으로 노드를 순회하는 방법이 있길래 사용해봤다.
도넛 구분법을 고민해서 dfs를 사용했던 것인데, 
이 방법에선 도넛을 세지 않고 다른 그래프 수를 구해서 빼는 방법으로 풀었다.
코드가 아주 간결해졌다.
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
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
