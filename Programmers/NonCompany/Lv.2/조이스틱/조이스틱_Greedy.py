# https://school.programmers.co.kr/learn/courses/30/lessons/42860
"""
constraints:

"""

def solution(name):
    alphabet_moves = 0
    for char in name:
        up_moves = ord(char) - ord('A')
        down_moves = ord('Z') - ord(char) + 1
        alphabet_moves += min(up_moves, down_moves)
    non_a_positions = [i for i, char in enumerate(name[1:], 1) if char != 'A']
    if not non_a_positions:
        return alphabet_moves
    n = len(name)
    right_only = max(non_a_positions)
    left_only = n - min(non_a_positions)
    cursor_moves = min(right_only, left_only)
    for i in range(len(non_a_positions) - 1):
        current_pos = non_a_positions[i]
        next_pos = non_a_positions[i + 1]
        move1 = current_pos * 2 + (n - next_pos)
        move2 = (n - next_pos) * 2 + current_pos
        cursor_moves = min(cursor_moves, move1, move2)
    return alphabet_moves + cursor_moves


inputdatas = [
    {"data": ["JEROEN"], "answer": 56},
    {"data": ["JAN"], "answer": 23},
    {"data": ["BABAABAA"], "answer": 8},
    {"data": ["AAAAAAAAAA"], "answer": 0},
    {"data": ["AAABAAAAB"], "answer": 7},
    {"data": ["BAAAAABAA"], "answer": 5},
    {"data": ["BAAABA"], "answer": 4},
    {"data": ["BBBABAABABABB"], "answer": 20},
    {"data": ["BBABAAAAAAB"], "answer": 9},
    {"data": ["BABBAABB"], "answer": 11},
    {"data": ["BBAAAAAAABAB"], "answer": 9},
    {"data": ["BAABBAAA"], "answer": 7},
]


"""
탐욕법(Greedy)
Lv.2. 현 시점 완료한 사람 21,625명, 정답률 38%
1차원 TSP인데 증명도 없고 블로그 풀이들은 자신들의 코드에서
A그룹 관통케이스가 어떻게 처리되고 있는지, 경계값이 어떻게 처리되는지도 모르는 것 같다.
일단 직관적인 방식으로 해보려고 BFS를 도입했는데 '인접'처리가 까다로워서 더러워졌다.
향후 다른 방법으로 풀어봐야겠다.

다른 풀이들은 알파벳 변환과 커서 이동을 한번에 처리했다.
나는 좀 더 직관적으로 풀기 위해 분리했고 non_a를 미리 구해서 while문을 없앴다.
또한 n-1이 아니라 직선이동 케이스를 미리 구해서 최소값을 정했다.
move1은 최초 위치에서 현재 위치로 왔다가 돌아가고 거꾸로 다음 알파벳까지 가는 것.
move2는 최초 위치에서 다음 알파벳부터 처리하고 돌아와서 현재까지 오는 것이다.
방향전환을 전제하고 있다.

기존 풀이들은 경계값이 비직관적으로 처리되고 있고, 사람들이 이를 인지조차 못하고 있는 듯 하지만
이 풀이에선 non_a만 탐색하고 non_a의 마지막 쌍까지만 처리하므로 훨씬 직관적이다.
또한 기존 풀이들이 인지하지 못하고 있는 '방향전환 없는 케이스'를 명시적으로 처리하여 이해를 도왔다.

엣지케이스를 고려하지 않고 풀이를 시도해야 쉽게 풀리는 케이스이고
실제로 풀이들이 대부분 비직관적으로 처리되고 있는 부분들을 언급조차 하지 않는다.
Lv.2로 책정되면 안되는 문제다.
항상 그렇듯 블로그 복붙 풀이들과 문제 개편 이전의 정답률이 영향을 준 듯 하다.
분석을 잘하는 사람은 오히려 풀기 힘들 것.
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
