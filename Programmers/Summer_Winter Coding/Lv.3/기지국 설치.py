# https://school.programmers.co.kr/learn/courses/30/lessons/12979
"""
전파 거리가 w면 설치된 아파트 좌우로 w만큼 전파가 퍼짐
일부 아파트에는 이미 기지국이 설치되어 있다.
모든 아파트에 전파를 전달하기 위해 증설해야 하는 기지국의 최소 개수를 리턴하라.

아파트 수 1 <= n <= 2 * 10^8
기지국이 설치된 아파트 번호가 담긴 1차원 배열 stations
1 <= stations <= 10^4
stations는 오름차순으로 정렬된 상태. 1 <= stations[i] <= n
1 <= w <= 10^4
"""


def solution(n, stations, w):
    cur = 1
    cnt = 0
    width = 2 * w + 1
    for mid in stations:
        ll, rr = mid - w, mid + w
        if cur < ll:
            num, denom = divmod(ll - cur, width)
            cnt += num + (1 if denom else 0)
        cur = rr + 1
    if cur < n + 1:
        num, denom = divmod(n + 1 - cur, width)
        cnt += num + (1 if denom else 0)
    return cnt


inputdatas = [
    [11, [4, 11], 1],
    [16, [9], 2],
]

"""
Summer/Winter Coding(~2018) 기출. 
Lv.3. 현 시점 완료한 사람 5,318명, 정답률 52%
20분 걸렸다.
처음에는 선분 겹침 문제가 생각났고, 그걸 활용할 방법이 생각나지 않았다.
dfs를 사용하기에는 아파트 수가 너무 많았다.
배열을 만들어서 커버하기에도 n이 너무 컸다.
그러다가 stations가 커버하지 못한 부분들을 
기지국 커버 범위로 나누어주면 쉽게 해결되지 않나 생각했고
해보니 그렇게 해결되었다.
나머지는 그 로직을 어떻게 문제에 적용시킬 것인가 였고, 
cur를 둬서 stations를 순회해준 후
남은 부분까지 체크하면 끝났다.

더 좋은 풀이가 있나 찾아봤는데 다른 풀이들도 거의 가 같은 로직을 사용했다.
"""

for t in inputdatas:
    print(solution(*t))
