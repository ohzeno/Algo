# https://school.programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    basket = []  # 뽑은 인형 넣을 바구니
    deleted = [0]  # 터진 인형 개수
    def push(data):
        # 바구니에 인형있고 제일 위 인형이 지금 넣는 인형과 같으면
        if basket and basket[-1] == data:
            basket.pop()  # 제일 위 인형 제거
            deleted[0] += 2  # 제거된 인형, 지금 넣으려던 인형 2개 터짐
        else:  # 바구니에 아무것도 없으면 그냥 넣기
            basket.append(data)

    height = len(board)
    def pick_up(n):
        for i in range(height):  # 위쪽부터 체크
            if board[i][n - 1]:  # 0이 아니면
                push(board[i][n - 1])  # 바구니에 넣고
                board[i][n - 1] = 0  # 제거
                return  # 더 볼 이유 없음.

    for move in moves:  # 크레인 작동.
        pick_up(move)
    return deleted[0]

inputdatas = [
    [
        [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]],
        [1, 5, 3, 5, 1, 2, 1, 4]
    ]
]

"""
2019 카카오 개발자 겨울 인턴십 기출. Lv.1. 
문제 읽고 인풋데이터 옮겨적기를 포함해 채점까지 12분 50초정도 걸렸다.
간단한 스택문제.
"""
for t in inputdatas:
    print(solution(t[0], t[1]))
