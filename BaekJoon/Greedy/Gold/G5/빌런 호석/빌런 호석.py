# https://www.acmicpc.net/problem/22251
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
디스플레이에 층수를 나타내는 K자리 수가 보임.
k=4이면 501은 0501이 됨
led 중 1~p개 반전시키려고 한다.
반전 후 1~n이 되도록 바꿀 것이다.
현재 엘리베이터가 x층에 있을 경우, 
빌런이 반전시킬 led를 고를 수 있는 경우의 수를 계산하라.
  0
1   2
  3
4   5
  6
"""
n, k, p, x = map(int, input().split())
n2t = {
    '0': (1, 1, 1, 0, 1, 1, 1),
    '1': (0, 0, 1, 0, 0, 1, 0),
    '2': (1, 0, 1, 1, 1, 0, 1),
    '3': (1, 0, 1, 1, 0, 1, 1),
    '4': (0, 1, 1, 1, 0, 1, 0),
    '5': (1, 1, 0, 1, 0, 1, 1),
    '6': (1, 1, 0, 1, 1, 1, 1),
    '7': (1, 0, 1, 0, 0, 1, 0),
    '8': (1, 1, 1, 1, 1, 1, 1),
    '9': (1, 1, 1, 1, 0, 1, 1)
}
def is_valid(cur):
    cnt = 0
    for i in range(k):
        aa, bb = xli[i], n2t[cur[i]]  # 각 층의 i번째 숫자
        for j in range(7):  # led 7개
            if aa[j] != bb[j]:
                cnt += 1
                if cnt > p:
                    return False
    return True  # 현재 층이 제외되었으므로 cnt == 0은 없다.
xli = [n2t[s] for s in str(x).zfill(k)]
ans = 0
for i in range(1, n+1):
    if i == x:  # 현재 층은 제외
        continue
    ans += is_valid(str(i).zfill(k))
print(ans)


"""
현 시점 골드 5. 제출 1297. 정답률 43.206%
정답률이 높은건 그냥 사람들이 다 블로그 정답 보고 풀어서 그렇다.
내 풀이보다 짧고 빠른 풀이들을 보니 죄다 
미리 숫자 사이 led 반전 수를 하드코딩 해놓은 같은 코드들이다.
톡방에서 나를 괴물이라 부르는 초보들이 저걸 쉽다고 하니 답이 나온다.
구현/브루트포스라고 분류되어 있지만 
led를 반전시키는 모든 경우의 수를 탐색하면 가지치기를 하더라도 시간초과가 발생한다.
적어도 내 풀이처럼 각 층 led끼리 비교해야 한다.
그래서 브루트포스가 아니라고 생각한다.
규칙 그대로 구현하는 것도 아니라 구현 문제라고 하기도 애매하다.
개인적으로는 그리디라고 본다.
"""