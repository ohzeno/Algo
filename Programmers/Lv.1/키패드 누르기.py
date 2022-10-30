# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    # 좌엄지 *, 우엄지 # 시작
    # 147은 좌엄지  369는 우엄지
    # 2580은 가까운 손가락
    # 거리 같으면 오른손잡이는 오른손 왼손잡이 왼손
    hand = 'L' if hand == 'left' else 'R'  # L, R로 문자열 변경.
    cnt = {
        'L': [3, 0],
        'R': [3, 2]
    }  # 손가락 현 좌표
    num_pos = {
        0: [3, 1],
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2]
    }  # 각 번호 좌표
    def dist(hand, num):  # 거리 체크하는 함수. 상하좌우로만 움직이니 가로세로 거리 더해준다.
        dis_y = abs(num_pos[num][0] - cnt[hand][0])
        dis_x = abs(num_pos[num][1] - cnt[hand][1])
        return dis_x + dis_y
    s = ''  # 정답 문자열
    for number in numbers:  # 번호 순회
        if number in [1, 4, 7]:  # 147은 왼손
            tmp = 'L'
        elif number in [3, 6, 9]:  # 369는 오른손
            tmp = 'R'
        else: # 그 외는 거리체크
            dis_l = dist('L', number)
            dis_r = dist('R', number)
            if dis_l < dis_r:  # 왼손이 가까우면 왼손
                tmp = 'L'
            elif dis_l > dis_r:  # 오른손이 가까우면 오른손
                tmp = 'R'
            else:  # 거리 같으면 자주 쓰는 손
                tmp = 'L' if hand == 'L' else 'R'
        s += tmp  # 정답에 더해주기
        cnt[tmp][0] = num_pos[number][0]  # 손가락 위치 갱신
        cnt[tmp][1] = num_pos[number][1]
    return s

inputdatas = [
    [[1,3,4,5,8,2,1,4,5,9,5], "right"],
    [[7,0,8,2,8,3,1,5,7,6,2], 'left'],
    [[1,2,3,4,5,6,7,8,9,0], 'right']
]

"""
2020 카카오 인턴십 기출. Lv.1 중간에 긴급재난문자 와서 시간체크가 이상하긴 한데 22분쯤 걸렸다.
num_pos를 일일이 입력하는게 귀찮긴 했지만 문제 자체는 쉬웠다.
베스트 풀이도 봤으나, 나와 같은 로직을 더 더럽게 푼 풀이라서 넘어간다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
