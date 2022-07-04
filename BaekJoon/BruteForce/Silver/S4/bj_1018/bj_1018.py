# https://www.acmicpc.net/problem/1018
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
mat = [input() for _ in range(n)]
answer = n * m  # 모든 블럭을 바꾸는 경우가 최대임.
for i in range(0, n - 8 + 1):
    for j in range(0, m - 8 + 1):
        # 8칸씩 잘라보는 모든 경우
        data = [mat[k][j:j+8] for k in range(i, i + 8)]
        default = ['W', 'B']
        change = [0, 0]
        for dft in range(2):  # 좌상단 W, B로 둬야할 경우 색칠 수 다 체크
            for n1 in range(8):  # 모든 행
                if n1 % 2 == 0:  # 행 인덱스가 0, 2, 4 등이면 0, 2, 4열 등이 디폴트여야함
                    for n2 in range(0, 8, 2):
                        if data[n1][n2] != default[dft]:
                            change[dft] += 1
                    for n3 in range(1, 8, 2):  # 1, 3, 5는 디폴트가 아니어야 함
                        if data[n1][n3] != default[(dft + 1) % 2]:
                            change[dft] += 1
                elif n1 % 2:  # 행 인덱스가 1, 3, 5 등이면 1, 3, 5열 등이 디폴트여야함
                    for n2 in range(1, 8, 2):
                        if data[n1][n2] != default[dft]:
                            change[dft] += 1
                    for n3 in range(0, 8, 2):
                        if data[n1][n3] != default[(dft + 1) % 2]:
                            change[dft] += 1
        if min(change) < answer:  # W, B 두 경우 최소값이 기존 최소값보다 작으면 최소값 갱신
            answer = min(change)
print(answer)
