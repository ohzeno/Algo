# https://www.acmicpc.net/problem/17829
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def compress(mat):
    n = len(mat)  # 현재 길이
    if n == 1:  # 압축 끝이면 숫자 반환
        return mat[0][0]
    new_mat = [[0] * (n // 2) for _ in range(n // 2)]  # 압축된 매트릭스
    for r in range(0, n//2):
        for c in range(0, n//2):
            lr, lc = r * 2, c * 2
            # 기존 매트릭스 2x2 블럭에서 원소 뽑아서 정렬, 두번째로 큰 값 추출해서 새 매트릭스에 입력
            tmp = [mat[lr][lc], mat[lr][lc + 1], mat[lr + 1][lc], mat[lr + 1][lc + 1]]
            tmp.sort()
            new_mat[r][c] = tmp[-2]
    return compress(new_mat)  # 압축반복

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
print(compress(mat))

"""
현 시점 실버2. 제출 2204.  정답률 74.852%
새 매트릭스와 기존 매트릭스의 인덱스만 잘 매칭해주면 쉽게 풀린다.
"""