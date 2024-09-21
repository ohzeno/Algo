# https://school.programmers.co.kr/learn/courses/30/lessons/81302
def solution(places):
    # 대기실은 5개. 각 대기실은 5x5 크기.
    # 응시자끼리 맨해튼거리 2 이하로 앉으면 안되지만
    # 응시자 사이에 파티션으로 막혀있을 경우에는 허용.
    # 키패드 2, 4 위치하고 1, 5가 파티션(대각선)이라도 허용
    # 맨해튼거리: T1, T2가 (r1, c1), (r2, c2)에 위치하면 |r1-r2| + |c1-c2|
    # P는 응시자, O는 빈 테이블, X는 파티션
    # 한 명이라도 지키지 않고 있으면 0, 다 지키고 있으면 1 반환
    # 각 행은 대기실. return 형식: 리스트에 대기실 순서대로 5개 숫자 담아 리턴.
    manhattan = []
    for y in range(-2, 3):
        for x in range(-2, 3):
            # 맨해튼 거리 2 이내, 자신 제외
            if -x - 2 <= y <= -x + 2 and x - 2 <= y <= x + 2 and (x or y):
                manhattan.append((y, x))

    def is_ok():
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':  # 사람 발견하면 주변 체크
                    for y, x in manhattan:
                        nr, nc = r + y, c + x
                        if 0 <= nr <= 4 and 0 <= nc <= 4 and place[nr][nc] == 'P':  # 범위 내, 사람인 경우만
                            if abs(y) + abs(x) == 1:  # 맨해튼거리 1이면 무조건 위반
                                return False
                            elif abs(y) == 2 and place[r + y//2][c] != 'X':  # 위아래 2면 사이에 칸막이 없으면 위반
                                return False
                            elif abs(x) == 2 and place[r][c + x//2] != 'X':  # 좌우 2면 사이에 칸막이 없으면 위반
                                return False
                            elif abs(x) == 1 and abs(y) == 1 and not (place[r][nc] == 'X' and place[nr][c] == 'X'):  # 대각선이면 사이에 칸막이 2개 없으면 위반
                                return False
        return True  # 위반자 없으면 True 반환

    answer = []
    for place in places:
        if is_ok():  # 위반자 없으면 1
            answer.append(1)
        else:  # 위반자 있으면 0
            answer.append(0)
    return answer

inputdatas = [
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ["POOOP", "OXXOX", "OXXPX", "OPXOX", "PXXXP"],
        ["PXXXX", "XPXXX", "XXXPP", "XXXXX", "XXXXX"]
    ]
]

"""
2021 카카오 채용연계형 인턴십 기출. Lv.2. 
49분 첫 제출. 테케 2~9, 11, 14~15, 17, 19~22, 27, 29~31 실패.
맨해튼 거리 배열 만들 때 0, 0을 제외하려고 if x * y를 넣어놨었다. 
하나만 0이라도 제외되어 버려서 오류 발생.
51분 (x or y)로 고친 후 통과.
꽤 번거로워서 오래 걸리는데 Lv.2가 맞나...?
다른 풀이들을 보니 dfs, bfs를 사용하거나 하드코딩 했다. 
확실히 dfs 사용하면 훨씬 빠르게 풀었을지도.
"""

for t in inputdatas:
    print(solution(t))
