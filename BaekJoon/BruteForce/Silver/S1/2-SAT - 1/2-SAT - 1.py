# https://www.acmicpc.net/problem/11277
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
2-SAT은 N개의 불리언 변수 
x_1, x_2, ..., x_n가 있을 때, 2-CNF 식을 true로 만들기위해 
x_i를 어떤 값으로 정해야하는지를 구하는 문제이다.

2-CNF식은 
 ( x V y ) ∧ ( ㄱ y V z ) ∧ ( x V ㄱ z ) ∧ ( z V y ) 와 같은 형태이다. 
여기서 괄호로 묶인 식을 절(clause)라고 하는데, 
절은 2개의 변수를 V한 것으로 이루어져 있다. 
V는 OR, ∧는 AND, ㄱ은 NOT을 나타낸다.

변수의 개수 N과 절의 개수 M, 그리고 식 f가 주어졌을 때, 
식 f를 true로 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.

예를 들어, N = 3, M = 4이고, 
f =  ( ㄱ x_1 V x_2 ) ∧ ( ㄱ x_2 V x_3 ) ∧ ( x_1 V x_3 ) ∧ ( x_3 V x_2 )  인 경우에 
x_1을 false, 
x_2을 false, 
x_3를 true로 정하면 식 
f를 true로 만들 수 있다. 하지만, N = 1, M = 2이고, 
f = ( x_1 V x_1 ) ∧ ( ㄱ x_1 V ㄱ x_1 ) 인 경우에는 
x_1에 어떤 값을 넣어도 식 f를 true로 만들 수 없다.

절은 두 정수 i와 j (1 ≤ |i|, |j| ≤ N)로 이루어져 있으며, 
i와 j가 양수인 경우에는 각각 
x_i, x_j를 나타내고, 
음수인 경우에는 
ㄱ x_i, ㄱ x_j를 나타낸다.
"""
from itertools import product
n, m = map(int, input().split())
clauses = [tuple(map(int, input().split())) for _ in range(m)]
for tf in product([1, 0], repeat=n):  # 참거짓 케이스 순회
    tf_d = dict(zip(range(1, n+1), tf))  # 해당 케이스 참거짓 딕셔너리
    for a, b in clauses:  # 절 순회
        c = tf_d[a] if a > 0 else not tf_d[-a]
        d = tf_d[b] if b > 0 else not tf_d[-b]
        if not (c or d):  # 절이 거짓이면 다음 케이스로. 각 절은 and로 이어져있기에.
            break
    else:  # 절이 모두 참이면 종료
        print(1)
        break
else:  # 모든 케이스가 거짓이면 0
    print(0)

"""
현 시점 실버 1. 제출 1427, 정답률 65.558%
입력파트 설명 '음수인 경우에는 ㄱ x_{-i}, ㄱ x_{-j}를 나타낸다.'때문에 조금 혼란스러웠다.
x_-i라는게 도대체 뭔가 했는데 예제를 직접 테스트해보니 그냥 ㄱ x_{-i}가 아니라 ㄱx_i라고 추정된다.
설명을 잘못 적어놓은듯.
처음엔 dfs를 사용하려 했는데
변수가 하필이면 숫자고, 음, 양이 나뉘어있는 귀찮은 케이스였다.
그래서 변수 세트를 만들고, 참거짓 케이스는 product로 중복조합을 사용했다.
둘을 조합해 참거짓 딕셔너리를 만들어서 절을 검사했다.
"""
