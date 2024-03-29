# https://www.acmicpc.net/problem/12850
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
숭실 대학교 정보 과학관은  캠퍼스의 길 건너편으로 유배를 당했다. 
그래서 컴퓨터 학부 학생들은 캠퍼스를 ‘본대’ 라고 부르고 정보 과학관을 ‘정보대’ 라고 부른다. 
준영이 또한 컴퓨터 학부 소속 학생이라서 정보 과학관에 박혀있으며 항상 본대를 가고 싶어 한다. 
어느 날 준영이는 본대를 산책하기로 결심하였다. 숭실 대학교 캠퍼스 지도는 아래와 같다.
https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12849/1.png
한 건물에서 바로 인접한 다른 건물로 이동 하는 데 1분이 걸린다. 
준영이는 산책 도중에 한번도 길이나 건물에 멈춰서 머무르지 않는다. 
준영이는 할 일이 많아서 딱 D분만 산책을 할 것이다.
(산책을 시작 한 지 D분 일 때, 정보 과학관에 도착해야 한다.) 
이때 가능한 경로의 경우의 수를 구해주자.
D 가 주어진다 (1 ≤ D ≤ 1,000,000,000)
가능한 경로의 수를 1_000_000_007 로 나눈 나머지를 출력한다.
"""
def mat_mul(A, B):
    return [
        [sum(a*b for a, b in zip(A_row, B_col)) % 1_000_000_007
         for B_col in zip(*B)]  # 행마다 열 순회
        for A_row in A  # 행 순회
    ]

def mat_pow(A, e):
    if e == 1:  # 1승이면
        return A
    if e % 2 == 1:  # 홀수승이면
        return mat_mul(A, mat_pow(A, e - 1))
    half = mat_pow(A, e // 2)  # 짝수승이면
    return mat_mul(half, half)

# 0: 정보과학관, 1: 전산관, 2: 미래관, 3: 신양관,
# 4: 한경직기념관, 5: 진리관, 6: 학생회관, 7: 형남공학관
mat = [[0, 1, 1, 0, 0, 0, 0, 0],
       [1, 0, 1, 1, 0, 0, 0, 0],
       [1, 1, 0, 1, 1, 0, 0, 0],
       [0, 1, 1, 0, 1, 1, 0, 0],
       [0, 0, 1, 1, 0, 1, 0, 1],
       [0, 0, 0, 1, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 1, 0, 1],
       [0, 0, 0, 0, 1, 0, 1, 0]]
print(mat_pow(mat, int(input()))[0][0])


"""
현 시점 골드 1. 제출 1497. 정답률 85.400%
본대 산책1의 풀이를 그대로 사용했다.
"""