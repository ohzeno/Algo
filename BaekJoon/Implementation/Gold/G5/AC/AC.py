# https://www.acmicpc.net/problem/5430
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
정수 배열 연산을 위한 언어 AC가 있다.
R은 배열에 있는 수의 순서를 뒤집는 함수, D는 첫 번째 수를 버리는 함수.
배열이 비어있는데 D를 사용하면 에러 발생.
함수는 조합해서 한 번에 사용 가능.
배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하라.
첫 줄에 테케 개수 T가 주어짐. T <= 100
수행할 함수 p. 1 <= len(p) <= 100,000
배열에 들어있는 수의 개수 n. 0 <= n <= 100,000
정수가 들어있는 배열이 주어진다. 원소 1 <= xi <= 100
전체 테케에서 주어지는 p의 길이 합과 n의 합은 70만을 넘지 않는다.
"""
from collections import deque


def solution():
    if p.count("D") > n:
        return "error"
    if not n:
        return "[]"
    arr = deque(data[1:-1].split(","))
    rev = False
    for f in p:
        match f:
            case "R":
                rev = not rev
            case "D":
                if rev:
                    arr.pop()
                else:
                    arr.popleft()
    if rev:
        arr.reverse()
    return f"[{','.join(arr)}]"


for _ in range(int(input())):
    p = input()
    n = int(input())
    data = input()
    print(solution())

"""
현 시점 골드 5. 제출 136484. 정답률 20.048 %
더 최적화된 방법이 있는 듯 하지만 직관적이지 않아 보여서 넘어간다.
백준 파이썬이 match를 지원하는 버전까지 올라왔다.
p를 받을 때 RR을 제거하는 것과 제거하지 않는 것은 크게 시간차이가 나지 않았다.
deque를 안쓰면 실행시간이 16배가 넘는다.
그냥 브루트포스랑 별 차이 없는데 이게 왜 골드인지 잘 모르겠다.
"""
