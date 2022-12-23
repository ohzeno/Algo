# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh
import sys
sys.stdin = open('input.txt')

for tc in range(10):
    c_num = int(input())
    row_s = []
    col_s = [0] * 100
    # dia_1 오른쪽 아래로 향하는 대각선.
    # dia_2 오른쪽 위에서 왼쪽 아래로 향하는 대각선
    dia_1 = dia_2 = 0
    # 매트릭스 만들기
    mat = [list(map(int, input().split())) for _ in range(100)]
    # 행 합 구하기, 대각선 합 구하기
    for i in range(100):
        row_s.append(sum(mat[i]))
        dia_1 += mat[i][i]
        dia_2 += mat[i][99 - i]
        # 열 합 구하기
        for j in range(100):
            col_s[j] += mat[i][j]
    # 합 리스트들 하나로 만들기
    total = row_s + col_s
    total.append(dia_1)
    total.append(dia_2)
    # 케이스별 최대 합 출력
    print('#{} {}'.format(c_num, max(total)))
