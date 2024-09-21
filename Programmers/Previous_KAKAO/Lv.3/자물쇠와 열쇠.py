# https://school.programmers.co.kr/learn/courses/30/lessons/60059
def solution(key, lock):
    # 1이 돌기 0이 홈. 회전 가능
    # 키와 자물쇠 모두 내가 보이는 방향 그대로 결합함.
    # 키는 len_key 자물쇠는 len_lock 크기. 키는 항상 자물쇠보다 작거나 같다.
    # 3 <= len < = 20. 둘 다 3~20
    len_key = len(key)
    len_lock = len(lock)

    def check(c_key):  # 자물쇠 크기에 맞춰진 키 단순 비교.
        for h in range(len_lock):
            for w in range(len_lock):
                # 키도 자물쇠도 1이면 충돌. 0 리턴
                if c_key[h][w] == 1 and 1 == lock[h][w]:
                    return 0
                # 자물쇠가 채워지지 않아도 0 리턴
                elif c_key[h][w] == 0 and lock[h][w] == 0:
                    return 0
        else:  # 자물쇠 채워지고 충돌 없으면 1 리턴
            return 1

    def shift(data, h, w):  # data를 아래로 h, 우로 w 밀어내기
        new_mat = []
        # w만큼 밀어내기 (열 채우기)
        for i in range(len_lock):  # len_lock 행 순회
            if w > 0:  # 오른쪽으로 밀고 왼쪽 0 채우기
                new_mat.append([0] * w + data[i][:-w])
            else:  # 왼쪽으로 밀면 오른쪽 0 채우기
                new_mat.append(data[i][-w:] + [0] * -w)
        for _ in range(-h if h < 0 else h):  # h(양수로 만들어서)회만큼 행 추가
            if h > 0:  # 아래로 밀고 위에 0 채우기
                new_mat.pop()
                new_mat.insert(0, [0] * len_lock)
            else:  # 위로 밀고 아래 0 채우기
                del new_mat[0]
                new_mat.append([0] * len_lock)
        return new_mat

    def rotate(data):  # 우로 90도 회전
        new_mat = []
        for h in range(len_key):  # 각 행마다
            tmp = []
            for w in range(len_key - 1, -1, -1):  # 마지막 인덱스부터 0까지
                tmp.append(data[w][h])  # 행 회전
            new_mat.append(tmp)  # 회전한 행 추가
        return new_mat

    def fill(data):
        dif = len_lock - len_key
        if dif == 0:  # 차이 없으면 그대로 리턴
            return data
        # 오른쪽 0 채우기
        new_mat = [data[i] + [0] * dif for i in range(len_key)]
        for _ in range(dif):  # 아래 dif줄만큼 0 채우기
            new_mat.append([0] * len_lock)
        return new_mat

    for r_c in range(4):  # 회전 수
        tmp_key = key  # 이전 회전 데이터 초기화
        if r_c:  # 회전 있으면 tmp_key 재할당
            for _ in range(r_c):  # r_c번만큼 회전
                tmp_key = rotate(tmp_key)
        tmp_key = fill(tmp_key)  # 회전했으면 0,0에 두고 자물쇠와 크기 맞추기.
        # 상, 좌로 미는건 자물쇠 한 칸 남도록 key
        for h in range(-(len_key - 1), len_lock):
            for w in range(-(len_key - 1), len_lock):
                 if check(shift(tmp_key, h, w)):  # 밀었을 때 정답이면 True 반환
                     return True
    return False  # 정답 없으면 거짓 리턴

inputdatas = [
    [[[0,0,1],
      [1,0,0],
      [0,0,0]],
     [[1, 1, 1, 1, 1],
      [1, 1, 0, 1, 1],
      [1, 0, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1]]],
    [[[1, 0, 1],
      [0, 1, 0],
      [1, 0, 1]],
     [[1,1,1],
      [1,1,1],
      [1,1,1]]],
    [[[0,0,0],
      [1,0,0],
      [0,1,1]],
     [[1,1,1],
      [1,1,0],
      [1,0,1]]]
]

"""
2020 카카오 공채 기출. Lv.3이지만 2시간 22분이나 소모했다.
효율성테스트가 없었고, 시간초과 걱정 없이 브루트포스로 풀 수 있었다.
2시간 22분만에 런타임에러까지 다 잡았다.
1시간 15분쯤 첫 로직 완성 후 런타임에러가 많았다.
로직 완성 자체도 시간이 오래 걸렸는데, 
브루트포스를 적용해보자고 생각하기 전에 시간효율을 생각하면 어떻게 
알고리즘을 만들어야 할 지 고민하느라 시간낭비가 심했다. 
결국 단순하게 회전, 사이즈 맞추기, 밀어내기, 열리는지 체크를 모두 따로 함수로 만들었다.
오류가 있나 살펴봤으나 찾지 못했고, 틀린게 아니라 런타임에러이기에 시간초과가 아닌가 의심했다.
시간을 줄이기 위해서 수정해보면서도, shift가 일일이 원소를 append, pop하고 있기에 
시간초과를 없애기 위해서는 로직을 갈아엎어야 하나 고민했다.
2시간 20분쯤 fill쪽에서 오류가 있다는걸 발견했다. fill 횟수를 줄이거나 하기 위해 작업했었으나
fill 자체의 문제가 있었던 것이다. 가로로는 lock과 key의 차이만큼 채워줬으나
세로로는 한 줄만 채워주고 있었다. 그래서 어딘가에서 인덱스 에러가 발생해 
런타임오류가 발생했을거라 추정된다.
오류 찾으며 질문들 살펴볼 때, 누군가가 이미 자물쇠가 열려있는게 있다고 해서 로직을 추가했으나
빼도 통과됐다. '자물쇠에는 홈이 파여있고'라고 묘사되었기에 
이미 열려 모두 돌기인 경우는 없는 것으로 파악된다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
