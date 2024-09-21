# https://school.programmers.co.kr/learn/courses/30/lessons/42894
def solution(board):
    # board는 NxN  N은 4~50
    # 각 행 원소는 0~200
    # 각 블록은 숫자로 표기.
    # 잘못된 블록 모양 주어지지 않음
    # 모양 상관없이 서로 다른 블록은 서로 다른 숫자로 표현됨.
    def type_check(r, c):
        """
        딕셔너리에
        제거 불가능한 블럭은 -1
        제거 가능한 블럭은 빈 칸 좌표 범위 입력
        """
        fail = 0
        # 윗줄 가로 2칸 이상
        if c < n - 1 and board[r][c] == board[r][c + 1]:
            fail = 1
        # ㅏ 형태.
        elif c < n - 1 and r < n - 2 and board[r][c] == board[r + 1][c + 1] and board[r][c] == board[r + 2][c]:
            fail = 1
        # ㅓ형태
        elif 0 < c and r < n - 2 and board[r][c] == board[r + 1][c - 1] and board[r][c] == board[r + 2][c]:
            fail = 1
        # __i 형태
        elif 1 < c and board[r][c] == board[r + 1][c - 2]:
            blocks[board[r][c]] = [r, [c - 2, c - 1]]
        # ㅗ형태
        elif 0 < c < n - 1 and board[r][c] == board[r + 1][c - 1] and board[r][c] == board[r + 1][c + 1]:
            blocks[board[r][c]] = [r, [c - 1, c + 1]]
        # _i형태
        elif 0 < c and r < n - 2 and board[r][c] == board[r + 2][c - 1]:
            blocks[board[r][c]] = [r + 1, [c - 1]]
        # ㄴ__ 형태
        elif c < n - 2 and board[r][c] == board[r + 1][c + 2]:
            blocks[board[r][c]] = [r, [c + 1, c + 2]]
        # ㄴ_ 형태
        elif board[r][c] == board[r + 2][c + 1]:
            blocks[board[r][c]] = [r + 1, [c + 1]]
        if fail:
            # 제거 불가능 블럭
            blocks[board[r][c]] = -1

    answer = 0
    n = len(board)
    blocks = {}
    rs = []  # 탐색시간 줄이기 위해 블럭이 있는 행만 기록
    for r in range(n):
        if not sum(board[r]):
            continue
        rs.append(r)
        for c in range(n):
            # 블럭이 존재하고 기록 안한 블럭이면 타입체크
            if board[r][c] and board[r][c] not in blocks:
                type_check(r, c)
    min_r = min(rs)  # 블럭이 존재하는 최 상단 행
    while True:
        suc = 0
        checked = []
        for r in rs:  # 블럭 존재하는 행만 체크
            for c in range(n):
                # 블럭이 존재하고, 제거 가능한 블럭이고, 체크했던 블럭이 아니라면
                if board[r][c] and blocks[board[r][c]] != -1 and board[r][c] not in checked:
                    fail = 0  # 제거 가능여부
                    val = board[r][c]
                    checked.append(val)  # 이미 체크한 블럭 등록
                    # 블럭 존재했던 최소 행부터 체크해야할 행까지
                    for cr in range(min_r, blocks[val][0] + 1):
                        if not fail:  # 이미 실패했으면 중단
                            for cc in blocks[val][1]:  # 체크해야할 열
                                if board[cr][cc]:  # 블럭 존재하면 실패
                                    fail = 1
                                    break
                    if not fail:  # 제거 가능하면
                        # 현재 행부터, 2줄 아래나 마지막 줄까지
                        for rr in range(r, min(r + 2, n - 1) + 1):
                            # 2줄 왼쪽이나 처음부터 2줄 오른쪽이나 오른쪽 마지막줄까지
                            for rc in range(max(0, c - 2), min(c + 2, n - 1) + 1):
                                if board[rr][rc] == val:  # 현재 블럭 제거
                                    board[rr][rc] = 0
                        suc = 1  # 성공 체크
                        answer += 1  # 제거한 블럭 추가
        if not suc:  # 전부 돌아도 성공이 없으면 현재 갯수 리턴
            return answer


inputdatas = [
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
     [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
     [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
     [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
     [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]],
    [[0, 0, 0, 0, 0],
     [1, 0, 0, 2, 0],
     [1, 2, 2, 2, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0]],
    [[0, 2, 0, 0],
     [1, 2, 0, 4],
     [1, 2, 2, 4],
     [1, 1, 4, 4]],
    [[0, 0, 0, 0, 0],
     [1, 0, 0, 2, 0],
     [1, 2, 2, 2, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0]],
    [[0, 0, 1, 1, 1],
     [0, 0, 0, 1, 0],
     [3, 0, 0, 2, 0],
     [3, 2, 2, 2, 0],
     [3, 3, 0, 0, 0]],
    [[0, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 1, 2, 0],
     [1, 2, 2, 2]],
    [[2, 2, 0, 0],
     [1, 2, 0, 4],
     [1, 2, 0, 4],
     [1, 1, 4, 4]],
    [[2, 2, 3, 3],
     [0, 2, 3, 0],
     [0, 2, 3, 0],
     [0, 0, 0, 0]],
]

"""
2019 카카오 공채 기출. Lv.4. 현 정답률 20%.
타입을 하드코딩할지 매번 체크할지 고민하며 문제풀이 방향성 잡는데까지 14분 30초 걸렸다.
61분 최초 제출. 테케 6~8, 10, 13~17 런타임 에러.
위쪽부터 체크하니 블럭이 나오면 해당 블럭 위쪽에 불가블럭이 있나 체크하도록 해뒀었다.
102
122
112  이런 형태에서 1을 체크할 때 2는 아직 딕셔너리에 들어가지 않는다.
터트리기 할 때 체크해주도록 변경. 괜히 효율성 생각하다 시간낭비한 케이스.
82분 2차 제출. 테케 6, 8, 16 런타임 에러.
type_check에서 r범위를 체크하지 않고 r+2를 체크하는 경우 발견. 수정.
93분 3차 제출. 통과.
어려운 문제는 아닌데 구현이 더러워서 정답률이 낮고 시간이 오래걸리는 문제다. 
SWEA스러운...백준에선 날먹 플레문제같은 부류.
시간만 단축할 수 있다면 점수따기 좋은 문제인데, 방법을 모르겠다.
다른 풀이들 중 짧은 것들을 보면 numpy를 사용했다.
행렬 연산을 배울 여유가 있을 때 numpy를 이용한 풀이를 해보기로 하고 지금은 넘어간다.
"""

for t in inputdatas:
    print(solution(t))
