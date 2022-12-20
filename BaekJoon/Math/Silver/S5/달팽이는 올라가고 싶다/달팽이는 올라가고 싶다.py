# https://www.acmicpc.net/problem/2869
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

clime, slide, height = map(int, input().split())
if height <= clime:
    print(1)
else:
    """
    공식화가 매우 어렵다. 30분은 걸렸고 체감난이도는 골드1 이상이었다.
    여러 케이스에서 height에 따라 변하는 결과를 적어서 나열해보면 공식화할 수 있다.
    연습장 없이는 풀지 못했을 것이다.
    """
    print(2 + (height - clime - 1) // (clime - slide))


