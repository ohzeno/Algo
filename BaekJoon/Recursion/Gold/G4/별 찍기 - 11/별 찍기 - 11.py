# https://www.acmicpc.net/problem/2448
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
첫째 줄에 N이 주어진다. 
N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)
첫째 줄부터 N번째 줄까지 별을 출력한다.
예제는 상단 문제 링크 참조
"""

def get_tree(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    half = n // 2
    half_tree = get_tree(half)
    margin = " " * half
    higher = []
    for line in half_tree:
        higher.append(margin + line + margin)
    for line in half_tree:
        higher.append(line + " " + line)
    return higher


n = int(input())
for line in get_tree(n):
    print(line)


"""
현 시점 골드 4. 제출 38701. 정답률 42.420 %
패턴에 공백 넣는 방법을 생각해내는게 좀 까다로웠다.
시간만 많이 잡아먹는 문제.
"""