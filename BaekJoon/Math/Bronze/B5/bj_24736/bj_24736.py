# https://www.acmicpc.net/problem/24736
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

ans = []
for _ in range(2):
    # 터치다운 필드골 세이프티 후점 전환
    t, f, s, p, c = map(int, input().split())
    ans.append(t * 6 + f * 3 + s * 2 + p + c * 2)
print(*ans)
