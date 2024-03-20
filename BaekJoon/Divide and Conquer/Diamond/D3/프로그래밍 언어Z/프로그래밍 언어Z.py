# https://www.acmicpc.net/problem/3203
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
프로그래밍 언어 Z에는 변수를 26가지 사용할 수 있다. 
이 변수는 모두 알파벳 소문자 (a-z)이고, 초기값은 0이다.

프로그램이 수행되는 동안 각 변수에는 0보다 크거나 같고, 9999보다 작거나 같은 정수만 저장할 수 있다. 만약, 범위를 넘어가는 값을 변수에 저장하려 한다면, 10,000으로 나눈 나머지를 저장한다.

프로그램의 각 줄에는 명령어가 하나만 등장하며, 아래 5가지 중 하나이다.
BEGIN	    프로그램의 가장 첫 줄에 나온다.
=	        연산자의 왼쪽에 있는 변수에, 오른쪽에 있는 식의 결과를 저장한다. 
            식은 하나 또는 그 이상의 덧셈, 뺄셈으로 이루어져 있고, 각 항은 상수 또는 변수이다.
            이때, 변수의 앞에 상수가 붙어있을 수도 있고 이때는 그 변수를 상수만큼 곱하면 된다.
            (a = 2b + 4 - c) 모든 연산자의 앞, 뒤는 공백이다. 상수는 0보다 크거나 같고, 
            999보다 작거나 같은 정수이다.
REPEAT n	블록의 시작을 나타내며, 그 블록을 n번 반복한다. (1 <= n <= 100,000)
STOP	    블록의 끝을 나타낸다.
PRINT var	변수 var에 저장되어 있는 값을 'var = value'와 같은 형태로 출력한다.
프로그래밍 언어 Z로 된 프로그램이 주어졌을 때, 화면에 출력되는 내용을 출력하는 프로그램을 작성하시오.
"""
class Matrix:
    def __init__(self, ir, ic, identity=False, varmat=False):
        self.r = ir
        self.c = ic
        if identity:  # 단위행렬
            self.mat = [[+(r == c) for c in range(self.c)] for r in range(self.r)]
        elif varmat:  # 변수행렬
            self.mat = [[0] for _ in range(self.r)]
            self.mat[26] = [1]  # 상수항
        else:  # 영행렬
            self.mat = [[0] * self.c for _ in range(self.r)]

    # 행 반환. 행만 반환하면 열은 수정할 수 있음.
    def __getitem__(self, idx):
        return self.mat[idx]

    # 행 자체를 수정하는건 setitem으로.
    def __setitem__(self, key, value):
        self.mat[key] = value

def get_var_idx(var: str) -> int:
    return ord(var) - 97  # 97은 'a'의 아스키코드

def compression() -> list[dict]:
    cmds = []  # 명령어 목록
    while True:  # 현 블럭 STOP 나올 때까지
        line = input()  # 명령어 입력
        if 'STOP' in line:  # 종료
            break
        elif 'REPEAT' in line:  # 반복문
            cmd = {
                'type': 'loop',
                'block': compression(),  # 반복문 내부 블록 압축. 재귀.
                'repeat': int(line.split()[1])
            }
        elif 'PRINT' in line:  # 출력문
            var = line.split()[1]
            cmd = {
                'type': 'print',
                'var_idx': get_var_idx(var),
                'var_name': var
            }
        else:  # 할당문
            cmd = {
                'type': 'assign',
                'trans_mat': make_trans(line)  # 변환행렬 생성
            }
        cmds.append(cmd)
        while cmds:
            # 할당문 하나만 있는 반복 블록인 경우 지수 압축.
            # 블록 내에 REPEAT이 있는 경우:
            #   재귀이므로 하위 블럭이 모두 압축된 후 while문에 진입.
            #   REPEAT 블록의 압축결과가 할당문 하나가 아니면 압축 불가
            # 블록 내에 PRINT가 있는 경우:
            #   할당 도중 PRINT해야하므로 할당 압축 불가
            if is_single_assign_loop(cmds[-1]):
                cmd = cmds.pop()
                trans = cmd['block'][0]['trans_mat']
                ex = cmd['repeat']
                new_cmd = {
                    'type': 'assign',
                    # 반복 횟수만큼 지수승
                    'trans_mat': mat_pow(trans, ex)
                }
                cmds.append(new_cmd)
            # 할당문이 연속되면 압축 가능
            elif len(cmds) >= 2 and is_chained_assign(cmds[-1], cmds[-2]):
                B = cmds.pop()['trans_mat']  # 두 번째 변환 행렬
                A = cmds.pop()['trans_mat']  # 첫 번째 변환 행렬
                new_cmd = {
                    'type': 'assign',
                    # 변환 행렬 A, B가 순서대로 실행되는 결과는
                    # 변환 행렬 C = B X A를 사용한 결과와 같음. 순서 주의.
                    'trans_mat': mat_mul(B, A)
                }
                cmds.append(new_cmd)
            else:  # 더 이상 압축할 수 없으면 종료
                break
    return cmds

def is_single_assign_loop(op: dict) -> bool:
    return (
        op['type'] == 'loop' and  # 반복문이고
        len(op['block']) == 1 and  # 블록 내 명령어가 하나이고
        op['block'][0]['type'] == 'assign'  # 그 명령어가 할당이면
    )

def is_chained_assign(op1: dict, op2: dict) -> bool:
    return op1['type'] == op2['type'] == 'assign'  # 둘 다 할당문이면 True

def make_trans(line: str) -> Matrix:
    toks = line.split()
    var_idx = get_var_idx(toks[0])  # 타겟 변수 인덱스
    coefs = [0] * 27  # 할당식 계수 리스트
    sign = 1  # 할당식 부호
    for tok in toks[2:]:
        if tok in '+-':  # 부호 변경
            sign = 1 if tok == '+' else -1
        else:  # 계수 갱신
            if 'a' <= tok[-1] <= 'z':  # 변수인 경우
                i = get_var_idx(tok[-1])
                coef = 1  # 변수 계수 기본값
                if tok[:-1]:  # 변수의 계수가 있으면 갱신
                    coef = int(tok[:-1])
            else:  # 상수인 경우
                i = 26
                coef = int(tok)  # 상수 계수 업데이트
            coefs[i] += sign * coef  # 계수 갱신
            coefs[i] %= 10000
    trans = Matrix(27, 27, identity=True)  # 단위행렬
    trans[var_idx] = coefs  # 타겟 변수 연산행 갱신
    return trans

def mat_mul(A: Matrix, B: Matrix) -> Matrix:
    C = Matrix(A.r, B.c)
    for i in range(A.r):
        for j in range(B.c):
            # 내적
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(A.c))
            C[i][j] %= 10000
    return C

def mat_pow(A: Matrix, ex: int) -> Matrix:
    if ex == 1:  # 1승이면
        return A
    if ex % 2 == 1:  # 홀수승이면
        return mat_mul(A, mat_pow(A, ex - 1))
    half = mat_pow(A, ex // 2)  # 짝수승이면
    return mat_mul(half, half)

def run_block(block: list, repeat=1) -> None:
    global var_mat
    for _ in range(repeat):  # 반복 실행
        for cmd in block:
            if cmd['type'] == 'loop':  # 루프 실행
                run_block(cmd['block'], cmd['repeat'])  # 내부 블럭 실행
            elif cmd['type'] == 'assign':  # 할당문 실행
                var_mat = mat_mul(cmd['trans_mat'], var_mat)  # 변수벡터 갱신
            elif cmd['type'] == 'print':  # 출력문 실행
                var = cmd['var_name']
                idx = cmd['var_idx']
                print(f'{var} = {var_mat[idx][0]}')

input()  # BEGIN 무시
var_mat = Matrix(27, 1, varmat=True)  # 변수벡터
run_block(compression())  # 압축된 코드 실행

"""
현 시점 ~~다이아4~~ 다이아 3으로 변경됨. 제출	375, 정답률 22.857%
스택 이용해서 그냥 구현하면 쉬운데, 시간제한이 빡빡하다.
싸피 시절에 그냥 구현했다가 시간초과가 발생했고
cpp솔루션 보고도 이해 못해서 고생했던 문제라 상담히 보람이 느껴진다.

REPEAT 9999
    x = 2x
이런거 9999번 반복하고 있으면 시간초과 발생한다.
할당문 최적화를 위해 행렬연산을 사용해야 한다.
선형대수에서 간단한 방정식을 계산할 때 변환행렬x변수벡터를 이용한다.
여기선 a~z 26개 변수와 상수항까지 적용하기 위해 길이 27의 변수벡터를 이용한다.
변환행렬끼리 연산하거나 거듭제곱을 통해 연산을 최대한 줄인 후 변수벡터와 곱해서
변수 벡터를 업데이트한다.
변환행렬 A, B를 순서대로 적용한 결과는 C = B x A를 사용한 결과와 같다.
행렬 연산은 순서에 영향을 받으니 순서를 바꾸면 안된다.

코드가 길고 프로그램이 복잡해서 최적화보다 가독성을 우선했다.
@cache를 mat_mul, mat_pow에 사용해봤으나 오히려 시간이 증가했다.
pow 자체가 간단한 거듭제곱 최적화를 거쳐서 중복연산이 거의 없어서 그런 듯 하다.
Strassen 거듭제곱 최적화 알고리즘에 대해서도 알게 됐지만 
행렬을 4등분, 재귀하므로 행/열이 2의 거듭제곱이어야 효과가 좋다.
추가 처리를 하더라도 행과 열이 몇백 이상인 경우에 효과적이고 
작은 행렬에 대해서는 오버헤드가 발생할 수 있다고 한다.
그리고 무엇보다 구현이 너무 복잡해서 코드가 난잡해진다.

선대 사용하는 문제가 고등학교 대회 문제라니...
"""