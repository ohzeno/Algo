# https://school.programmers.co.kr/learn/courses/30/lessons/60062
from collections import deque

# dfs 풀이.
def solution0(n, weak, dist):
    # 레스토랑 리모델링 중 주기적으로 외벽 상태 점검.
    # 레스토랑은 원 모양. 외벽 둘레 n m. 추위가 심할 경우 손상될 수 있는 취약지점 존재.
    # 점검 시간 1시간 제한. 1시간 이동 거리 사람마다 다름.
    # 최소한의 사람을 투입해 취약 지점 점검, 나머지는 내부 공사.
    # 레스토랑 정북 방향 0. 취약지점 위치는 정북으로부터 시계방향으로 떨어진 거리 나타냄.
    # 점검 인원은 시계/반시계 방향으로 외벽 따라서만 이동.
    # n: 외벽 길이. 1~200
    # weak: 취약지점 담긴 배열. 1~15. 원소는 0~n-1. 오름차순 정렬되어있음.
    # dist: 각 사람 1시간 이동거리.  1~8. 원소는 1~100
    # 점검 위해 보내야 하는 사람 수 최소값 리턴.
    # 모두 투입해도 전부 점검 불가하면 -1 리턴
    def check(st, weak, d):
        if d >= n - 1:  # 이러면 어디서 출발하든 전부 체크함.
            return []
        rcheck = []
        # 시계방향 체크. 정북 안넘은 범위, 정북 넘었을 경우 0~넘은 범위에 속하는 경우
        # 해당 사례들은 체크됐으므로 제거함.
        for w in weak:
            if st <= w <= st + d or (w < st and w <= st + d - n):
                rcheck.append(w)
        for v in rcheck:
            weak.remove(v)
        return weak

    def dfs(cur, weak):
        if cur > min_people[0]:  # 최소 인원 초과하면 체크X
            return
        if not weak or cur >= over:  # 전부 체크했거나 남은 인원 없으면
            if not weak and cur < min_people[0]:  # 전부 체크한 경우만 최소인원 갱신
                min_people[0] = cur
            return
        for st in weak:
            remain = check(st, weak.copy(), dist[cur])
            tr = tuple(remain)
            if (cur, tr) not in visited:  # 남아있고, 이미 체크했던 취약점 배열이 아닌 경우만
                visited.add((cur, tr))  # 방문처리
                dfs(cur + 1, remain)  # 다음 인원으로 체크하도록

    visited = set()
    visited.add((0, tuple(weak)))
    dist.sort(reverse=True)
    over = len(dist)
    min_people = [over + 1]  # 최대 인원보다 많음.
    dfs(0, weak)
    if min_people[0] == over + 1:  # 다 돌아도 갱신 안됐으면 체크 못함.
        return -1
    else:
        return min_people[0]

# bfs 풀이
def solution1(n, weak, dist):
    # 레스토랑 리모델링 중 주기적으로 외벽 상태 점검.
    # 레스토랑은 원 모양. 외벽 둘레 n m. 추위가 심할 경우 손상될 수 있는 취약지점 존재.
    # 점검 시간 1시간 제한. 1시간 이동 거리 사람마다 다름.
    # 최소한의 사람을 투입해 취약 지점 점검, 나머지는 내부 공사.
    # 레스토랑 정북 방향 0. 취약지점 위치는 정북으로부터 시계방향으로 떨어진 거리 나타냄.
    # 점검 인원은 시계/반시계 방향으로 외벽 따라서만 이동.
    # n: 외벽 길이. 1~200
    # weak: 취약지점 담긴 배열. 1~15. 원소는 0~n-1. 오름차순 정렬되어있음.
    # dist: 각 사람 1시간 이동거리.  1~8. 원소는 1~100
    # 점검 위해 보내야 하는 사람 수 최소값 리턴.
    # 모두 투입해도 전부 점검 불가하면 -1 리턴
    def check(st, weak, d):
        if d >= n - 1:  # 이러면 어디서 출발하든 전부 체크함.
            return ()
        # 시계방향 체크. 정북 안넘은 범위, 정북 넘었을 경우 0~넘은 범위에 속하는 경우
        # 해당 사례들은 체크됐으므로 not으로 제외함.
        return tuple(filter(lambda x: not (
                st <= x <= st + d or (x < st and x <= st + d - n)
        ), weak))

    dist.sort(reverse=True)  # 활동범위 넓은 사람부터 체크
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))
    for cur, d in enumerate(dist):  # 각 사람마다 모든 경우의 수 체크를 위해 for문.
        for _ in range(len(q)):  # 현 사람 모든 경우 체크한 후 다음으로 넘어가기 위해 for문.
            now_weak = q.popleft()  # 왼쪽부터 뽑아야함.
            # 1번 체크하고 2번 남았는데 3번부터 체크하면 의미없음.
            for st in now_weak:  # 그래서 순서대로 체크.
                remain = check(st, now_weak.copy(), d)  # 검사하고 남은 취약점
                if not remain:  # 안남았으면 bfs이므로 최소인원임. 리턴
                    return cur + 1
                elif remain not in visited:  # 남아있고, 이미 체크했던 취약점 배열이 아닌 경우만
                    visited.add(remain)  # 방문처리
                    q.append(list(remain))  # 다음 인원으로 체크하도록
    return -1

inputdatas = [
    [12, [1, 5, 6, 10], [1, 2, 3, 4]],
    [12, [1, 3, 4, 9, 10], [3, 5, 7]],
    [200, [0, 100], [1, 1]],
    [200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]],
    [16, [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15], [4, 2, 1, 1]]
]

"""
2022 카카오 공채 기출. Lv.3
58분에 초안 제출했고, 5, 8, 10, 11, 12, 14, 15, 19, 21 테케를 실패했다.
내 풀이는 시작 지점, 방향에 따라 최대 체크 수를 달성하면 방향이나 위치에 상관없이 다음 사람으로 넘어갔다.
아마 한 사람 자체에서는 방향과 시작지점 상관없이 같은 수의 취약점을 체크할 수 있어도
남은 취약점에 따라 사람 수에 차이가 생기는 케이스들이 있을거라 생각된다.
실행시간을 줄이려고 저렇게 짠건데 결국 dfs를 작성하게 됐다.
38분 뒤 dfs를 제출했고 
3, 4, 6, 10, 11, 12, 13, 14, 15, 17 케이스에서 시간초과가 발생했다.
방향을 전부 dfs하지 않고, 많은 취약점을 처리할 수 있는 방향(처리할 수 있는 취약점 수가 같으면 둘 다)을 dfs하도록 바꿔서 제출했고
3, 4, 10, 11, 12, 13, 14 케이스에서 시간초과가 발생했다.
어차피 취약점을 전부 st지점으로 지정하기에, 1에서 11로 반시계 방향을 체크하지 않더라도 11에서 1로 시계방향에서 체크가 되기에 한 방향만 체크하도록 바꿨다.
10, 11, 12, 13, 14 케이스에서 시간초과가 발생했다.
알고보니 각 사람 별 모든 경우의 수에서 weak이 겹치는 경우가 많았다.
weak이 같고 다음 사람이 같으면 이전 경로와 상관없이 같은 케이스가 되니 중복체크할 필요가 없다.
visited로 처리해주니 dfs, bfs 모두 통과했다.
"""

for t in inputdatas:
    print(solution0(t[0], t[1], t[2]))


