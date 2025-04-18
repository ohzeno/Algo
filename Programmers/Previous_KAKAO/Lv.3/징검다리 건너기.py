# https://school.programmers.co.kr/learn/courses/30/lessons/64062
"""
constraints:

"""


def solution(stones, k):
    """
    디딤돌 숫자는 밟을 때마다 줄어듦
    살아있는 돌 가장 가까운거 밟아야함
    최대 뛸 수 있는 칸은 k. 3칸이면 1에서 4까지.
    최대 몇 명 건널 수 있는지 리턴
    설명엔 없는데 시작, 끝도 생각해야 할듯
    """
    if k == 1:  # k가 1이면 모든 돌을 건너야 하므로 최소값만큼 건널 수 있음.
        return min(stones)
    n = len(stones)
    if n == k:
        # k와 n이 같으면 하나의 돌만 밟으면 되므로 최대값만큼 건널 수 있음.
        return max(stones)
    if all(stones[i-1] >= stones[i] for i in range(1, n)):
        # 역정렬된 케이스는 끝에서 가장 멀리 뛸 수 있는 돌의 값만큼 건널 수 있음.
        # 엣지케이스. 따로 처리 안하면 효율성 시간초과됨.
        return stones[-k]
    min_of_max = 2e8  # 원소 최대값이 2억
    i = -1  # 출발점은 돌이 아님.
    # 각 점프 구간 최대값들 중 최소값이 정답.
    while i < n - k:  # +1은 출발점. n - k부터는 건너뛰면 도착.
        max_idx, max_stone = -1, 0
        for j in range(i+1, i+1+k):  # k는 위에서 처리했음. 출발 돌 제외해서 i+1까지만.
            if max_stone < stones[j]:
                max_idx, max_stone = j, stones[j]
        if max_stone == 1:  # 구간 최대값이 1이면 한 명 이상 지날 수 없음.
            return 1
        min_of_max = min(min_of_max, max_stone)
        i = max_idx
    return min_of_max


inputdatas = [
    {"data": [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3], "answer": 3},
    {"data": [[2, 2, 4, 3, 4, 1, 4, 3, 5, 1], 3], "answer": 4},
    {"data": [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10], "answer": 10},
    {"data": [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 3], "answer": 3},
    {"data": [[2, 2, 2, 2, 2], 3], "answer": 2}
]


"""
2019 카카오 개발자 겨울 인턴십
Lv.3. 현 시점 완료한 사람 8,746명, 정답률 49%
정확성 테스트에 오류가 있다. k = len(stones)이면 원소 중 최댓값이 정답이지만
최솟값을 반환하더라도 정확성 테스트를 모두 통과한다. <- 이건 옛날에도 그랬는데 지금도 그렇다.
효율성 13번 테케 때문에 무조건 이분탐색을 사용해야 한다는 말이 많았다.
실제로 넷상의 풀이는 내가 찾은 몇십 개 모두 이분탐색이었다.
나는 슬라이딩 윈도우를 사용하되, 예외 처리를 해주어서 모두 통과했다.

다시 풀면서 미세한 최적화와 가독성 개선만 해줬다. 저번 풀이가 큰 틀에서 좋았다.
3회차. dp로 풀어보려다가 실패하고 다시 내 풀이로 돌아왔다.
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
