# https://www.acmicpc.net/problem/1629
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
자연수 A를 B번 곱한 수를 알고 싶다. 
단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
"""
a, b, c = map(int, input().split())
print(pow(a, b, c))  # 내장함수

def solution(a, b, c):  # 분할정복. 함수 밖에서 %를 사용하면 시간초과가 발생한다. 요상...
    if b == 1:
        return a % c
    else:
        tmp = solution(a, b // 2, c)
        if b % 2 == 0:
            return tmp * tmp % c
        else:
            return tmp * tmp * a % c
print(solution(a, b, c))
# if a > c:
#     print(a % c)
# else:
#     b -= 1
#     cur = a
#     while b:
#         cur *= a
#         b -= 1
#         if cur > c:
#             cur %= c
#     print(cur)

"""
현 시점 실버1. 제출 89155, 정답률 26.457%
나름대로 규칙을 찾아보니, a가 c보다 크면 제곱할 필요 없이 그냥 a % c를 출력하면 된다.
a가 c보다 작은 경우 제곱을 진행하며 c보다 커질 때마다 c로 나눈 나머지로 초기화한다. 
남은 a를 다 곱하고 c로 나눈 나머지를 출력하면 된다. 
ex) 3 4 5면 9%5 = 4이니
 (((4 * 3) % 5) * 3) % 5 = 1이 정답이다.
하지만 이 방법을 사용하니 시간초과가 발생했다.

문제 자체를 잘못 이해했다. a**b%c를 구하는 도중에 숫자가 커지는 것을 우려하는 건줄 알았는데
a**b 자체가 커지는 것을 우려하는 것이었다.

거듭제곱의 분할정복으로 사용하는 일반적인 방법을 배워 사용했고
python 자체의 pow에도 a**b%c를 구하는 기능이 내장되어 있었고, 
상당히 빨라서 시간초과 하지 않고 통과한다.

거듭제곱의 분할정복 경우에 함수 내에서 % c를 하면 40ms로 통과하지만
함수 밖에서 % c를 하면 500ms를 초과해서 시간초과가 발생한다.
같은 연산 한 번인데 왜 저렇게 어마어마한 시간차이가 발생하는지 의아하다...
"""