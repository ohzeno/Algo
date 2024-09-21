# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    """
    왼손 *, 오른손 #에서 시작
    상하좌우로만 이동 가능. 키패드 한 칸 이동 거리 1
    147 왼손, 369 오른손, 2580은 키패드에서 가까운 엄지 사용.
    거리가 같으면 주 손 사용.
    누를 번호 배열과 주 손이 주어질 때, 각 번호를 누를 손을 연속된 문자열로 반환하라.
    """
    hand = 'L' if hand == 'left' else 'R'  # L, R로 문자열 변경.
    h_pos = {'L': [3, 0], 'R': [3, 2]}  # 손가락 현 좌표
    pos_dic = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1]
    }  # 각 번호 좌표
    def cal_dist(h, num):  # 거리 체크하는 함수. 상하좌우로만 움직이니 가로세로 거리 더해준다.
        return abs(h_pos[h][0] - pos_dic[num][0]) + abs(h_pos[h][1] - pos_dic[num][1])
    s = ""
    for num in numbers:
        if num in [1, 4, 7]:  # 147은 왼손
            tmp = "L"
        elif num in [3, 6, 9]:  # 369는 오른손
            tmp = "R"
        else:  # 그 외는 거리체크
            l_d = cal_dist('L', num)
            r_d = cal_dist('R', num)
            if l_d < r_d:  # 왼손이 가까우면 왼손
                tmp = "L"
            elif l_d > r_d:  # 오른손이 가까우면 오른손
                tmp = "R"
            else:  # 거리가 같으면 주 손
                tmp = hand
        s += tmp  # 정답에 더해주기
        h_pos[tmp] = pos_dic[num]  # 손가락 위치 갱신. 값 수정할 게 아니라서 리스트 째로 대입해도 괜찮음.
    return s


inputdatas = [
    [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"],
    [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"]
]

"""
2020 카카오 인턴십 기출. Lv.1 중간에 긴급재난문자 와서 시간체크가 이상하긴 한데 22분쯤 걸렸다.
num_pos를 일일이 입력하는게 귀찮긴 했지만 문제 자체는 쉬웠다.
베스트 풀이도 봤으나, 나와 같은 로직을 더 더럽게 푼 풀이라서 넘어간다.

2차 시도. 쉬운 문제이기도 하고 비교적 최근에 풀어서 그런지 2차 풀이가 오히려 
난잡해진 부분도 있다. 그래도 로직은 같고 1~2 줄 차이 정도다. 잠깐 훑어보면 개선 가능한 정도. 
9분 정도 걸렸다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
