# https://www.acmicpc.net/problem/1307
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline()

"""
n이 주어지면 nxn 마방진을 만들어라.
가로, 세로, 대각선의 합이 모두 같아야한다.
"""
def odd_s(n):
    """
    시암의 방법.
    음수 a에 대해 a%b라고 하면
    a보다 작거나 같고 abs(c)가 b의 배수인 c를 구하고
    a-c가 a%b의 결과가 된다.
    0행에서 상단으로 넘어가면 (0-1)%n = n-1이 되므로 최하단 행으로 간다.
    """
    mat = [[0] * n for _ in range(n)]
    r, c = 0, n//2
    for i in range(1, n**2 + 1):
        mat[r][c] = i
        nr, nc = (r-1) % n, (c+1) % n  # 우상단
        if mat[nr][nc]:  # 우상단이 비어있지 않으면 아래로
            nr, nc = (r+1) % n, c
        r, c = nr, nc
    return mat

def four_s():
    """
    4의 배수인 경우 n//4 사이즈 셀로 나눈다.
    대각선 셀 제외하고 상하, 좌우 반전하면 끝.
    """
    mat = [[0] * n for _ in range(n)]
    cnt = 1
    # 1부터 n**2까지 초기화
    for r in range(n):
        for c in range(n):
            mat[r][c] = cnt
            cnt += 1
    ss, ed = n//4, n-1  # sell size, end
    for r in range(ss):
        for c in range(ss * 2):
            # (0,1)<->(3,2), (0,2)<->(3,1). 상하영역 반전
            mat[r][ss+c], mat[ed-r][ed-ss-c] = mat[ed-r][ed-ss-c], mat[r][ss+c]
            # (1,0)<->(2,3), (2,0)<->(1,3). 좌우영역 반전
            mat[ss+c][r], mat[ed-ss-c][ed-r] = mat[ed-ss-c][ed-r], mat[ss+c][r]
    return mat

def other_s():
    """
    4의 배수가 아닌 짝수인 경우
    """
    half = n//2
    half_s = odd_s(half)  # 절반 크기 마방진
    mat = {i: [[0] * half for _ in range(half)] for i in range(1, 5)}  # 4등분 배열(4분면)
    l_bnd, scale = n//4, half**2
    r_bnd = half - l_bnd + 1
    for r in range(half):
        for c in range(half):
            k = 4 if (r != l_bnd and c < l_bnd) or (r == l_bnd and 0 < c <= l_bnd) else 3
            mat[k][r][c] = 3  # 3, 4사분면
            val = 1 if r_bnd <= c else 2  # 1, 2사분면
            mat[1][r][c], mat[2][r][c] = val, 3-val  # 1과 2를 반전
            for k in mat:  # 4등분 배열에 대해
                mat[k][r][c] = mat[k][r][c] * scale + half_s[r][c]  # scale 곱하고 절반 크기 마방진 더하기
    for i in range(half):  # 좌우 합치기
        mat[4][i] += mat[1][i]
        mat[3][i] += mat[2][i]
    return mat[4] + mat[3]  # 상하 합치기

n = int(input())
if n % 2:  # 홀수
    ans = odd_s(n)
elif n % 4 == 0:  # 4의 배수
    ans = four_s()
else:  # 4의 배수가 아닌 짝수
    ans = other_s()
for r in ans:
    print(*r)

"""
현 시점 플래4. 제출 765. 정답률 35.638%
애드 혹으로 분류되어 있지만
마방진 구현방법을 문제 푸는 사람이 만들 수는 없으니
구현으로 봐야할 것 같다.
홀수, 4의 배수, 4의 배수가 아닌 짝수 각각에 대해 구현방법이 있고
그걸 그대로 적용해서 통과했다.
이후 최적화를 거쳐
코드 길이를 2148B에서 1475B로 줄였고
시간을 92ms에서 84ms로 줄였다.
"""