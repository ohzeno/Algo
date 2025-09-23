# https://school.programmers.co.kr/learn/courses/30/lessons/42860
"""
constraints:

"""
from collections import deque


def solution(name):
    # 1. 알파벳 변경 비용
    alphabet_moves = 0
    for char in name:
        up_moves = ord(char) - ord('A')
        down_moves = ord('Z') - ord(char) + 1
        alphabet_moves += min(up_moves, down_moves)
    # A가 아닌 위치들 찾기
    non_a_positions = [0] + [i for i, char in enumerate(name[1:], 1) if char != 'A']
    non_a_positions = sorted(list(set(non_a_positions)))

    if len(non_a_positions) == 1:
        return alphabet_moves

    pos_to_idx = {pos: idx for idx, pos in enumerate(non_a_positions)}
    n = len(name)
    initial_indices = set(range(1, len(non_a_positions)))
    q = deque([(0, frozenset(initial_indices), 0)])
    visited_states = {(0, frozenset(initial_indices)): 0}

    # 2. 커서 이동 비용
    cursor_moves = float('inf')
    while q:
        cur, unvisited_indices, move_cnt = q.popleft()
        if not unvisited_indices:
            cursor_moves = min(cursor_moves, move_cnt)
            continue
        cur_idx = pos_to_idx[cur]

        unvisited_list = sorted(unvisited_indices)
        # 인접 노드 찾기
        adjacent_indices = []

        # 왼쪽 인접
        left_candidates = [idx for idx in unvisited_list if idx < cur_idx]
        if left_candidates:
            adjacent_indices.append(max(left_candidates))
        else:
            if unvisited_list:
                adjacent_indices.append(max(unvisited_list))

        # 오른쪽 인접
        right_candidates = [idx for idx in unvisited_list if idx > cur_idx]
        if right_candidates:
            adjacent_indices.append(min(right_candidates))
        else:
            if unvisited_list:
                adjacent_indices.append(min(unvisited_list))

        adjacent_indices = list(set(adjacent_indices))

        # 가까운 인접 노드로 이동
        for next_idx in adjacent_indices:
            next_pos = non_a_positions[next_idx]
            right_dist = (next_pos - cur) % n
            left_dist = (cur - next_pos) % n
            min_dist = min(right_dist, left_dist)
            new_moves = move_cnt + min_dist
            new_unvisited = frozenset(unvisited_indices - {next_idx})
            state = (next_pos, new_unvisited)

            if state not in visited_states or visited_states[state] > new_moves:
                visited_states[state] = new_moves
                q.append((next_pos, new_unvisited, new_moves))

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
레벨 잘못 책정된 문제들이 으레 그렇듯, 오히려 생각을 어설프게 해야 쉬운 문제.
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
