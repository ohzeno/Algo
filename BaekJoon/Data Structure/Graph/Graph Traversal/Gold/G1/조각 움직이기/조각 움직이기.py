# https://www.acmicpc.net/problem/1035
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
"""

from collections import deque


def solve():
    board = []
    pieces = []
    for r in range(5):
        board.append(input())
        for c in range(5):
            if board[-1][c] == '*':
                pieces.append((r, c))
    if is_connected(pieces):
        return 0
    q = deque([(tuple(pieces), 0)])
    visited = {tuple(pieces)}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        cur_pieces, moves = q.popleft()
        # 각 조각을 하나씩 이동해보기
        for i in range(len(cur_pieces)):
            x, y = cur_pieces[i]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 범위 체크, 다른 조각과 충돌하지 않는지 체크
                if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in cur_pieces:
                    # 새로운 상태 만들기
                    new_pieces = list(cur_pieces)
                    new_pieces[i] = (nx, ny)
                    new_state = tuple(sorted(new_pieces))
                    if new_state not in visited:
                        # 연결되었는지 체크
                        if is_connected(new_pieces):
                            return moves + 1
                        visited.add(new_state)
                        q.append((new_state, moves + 1))
    return None


def is_connected(pieces):
    if len(pieces) <= 1:
        return True
    visited = set()
    stack = [pieces[0]]
    visited.add(pieces[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pieces_set = set(pieces)
    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in pieces_set and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append((nx, ny))
    return len(visited) == len(pieces)


print(solve())


"""
현 시점 Gold I. 제출 2412. 정답률 47.671 %
bfs + dfs
"""
