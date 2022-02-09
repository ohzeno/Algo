# https://www.acmicpc.net/problem/9663
import sys

sys.stdin = open("input.txt")

""" 
본래 N퀸즈는 백트래킹 문제이며 백준에서도 백트래킹, 브루트포스로 분류되어 있으나
파이썬으로는 전처리를 하지 않으면 시간초과를 해결할 방법이 보이지 않는다.
처음에 2차원 배열로 방문행렬까지 만들어서 처리하다가 재귀초과, 메모리초과.
이후 아래 코드로 바꿨고 input이 느리니 sys.stdin.readline()도 사용해봤으나
더 최적화할 방법이 생각나지 않는다. 
다른 정답코드들은 그냥 정답을 미리 적어놓고 print하도록 해뒀다...
PyPy3나 다른 언어로만 통과 가능.
"""
def dfs(y):
    global res
    if y == n:  # n-1이 마지막줄.
        res += 1
        return
    # 열 순회
    for i in range(n):
        # y행 i(0~n)열에 퀸을 놓겠다.
        # i 바뀔때마다 갱신되니 visited 필요X
        rows[y] = i
        # 0 ~ y-1행까지 놓은 퀸과 지금(y행) 놓은 퀸의 열이 겹치는가?
        # 혹은 열 차이 절댓값이 행차이와 같은가? = 대각선 겹침
        # 그런 경우 break로 안쪽 for문 깨고 다음 i(열) 체크
        for j in range(y):
            if rows[y] == rows[j] or \
                    abs(rows[j] - rows[y]) == y - j:
                break
        # 겹치지 않으면 다음 행 체크
        else:
            dfs(y + 1)


n = int(input())
res = 0
rows = [0] * n
dfs(0)  # n*n 줄에 n개 놓는거라 한 줄에 무조건 하나 들어감
print(res)
