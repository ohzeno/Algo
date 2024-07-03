# https://www.acmicpc.net/problem/28702
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
i가 3의 배수 and 5의 배수: FizzBuzz
i가 3의 배수 and not 5의 배수: Fizz
i가 not 3의 배수 and 5의 배수: Buzz
i가 not 3의 배수 and not 5의 배수: i
연속으로 출력된 세 개의 문자열이 주어진다.
다음에 올 문자열은?
"""

for i in range(3):
    s = input()
    if s.isdigit():
        n = int(s) + (3 - i)
        break
is_fizz = n % 3 == 0
is_buzz = n % 5 == 0
ans = ''
if is_fizz:
    ans += 'Fizz'
if is_buzz:
    ans += 'Buzz'
if not is_fizz and not is_buzz:
    ans = n
print(ans)


"""
현 시점 브론즈 1. 제출 2958. 정답률 65.157 %
i가 3의 배수, 5의 배수가 아닌 문자열이 셋 연속으로 올 가능성을 검토해야 한다.
i, i+1, i+2
i가 3의 배수가 아닐 경우, 임의의 n에 대해 3n+1, 3n+2로 둘 수 있다.
첫 케이스면 i+2가 3의 배수가 되며
두 번째 케이스면 i+1이 3의 배수가 된다.
그러므로 모든 케이스는 세 줄 중 하나는 숫자가 주어진다.
문제 조건에서는 '여러 문자열이 올 수 있는 경우'라고 해서 
문자열만 연속되고, 여러 케이스에 매칭되는 경우를 고려하게 만들지만
셋 중 하나가 숫자라면 네번째 i가 정해지므로 출력은 그것만 고려하면 된다.
이과 입장에선 쉽긴 한데, 브론즈 1 치고는 수학이 좀 들어가는 문제인듯.
"""