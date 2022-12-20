# https://www.acmicpc.net/problem/2561
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def swap(data_s, a, b):
    a -= 1
    data_s1 = data_s[:a]
    data_s2 = data_s[a:b]
    data_s3 = data_s[b:]
    return data_s1 + data_s2[::-1] + data_s3

def front_find(data_f):  # 왼쪽부터 탐색
    st_f, ed_f = None, None
    for i in range(N):
        if data_f[i] != sol[i]:
            st_f = i + 1
            for j in range(i + 1, N):
                if data_f[j] == sol[i]:
                    ed_f = j + 1
                    return st_f, ed_f
    if st_f == None and ed_f == None:
        return 1, 1

def back_find(data_b):
    st_b, ed_b = None, None
    for i in range(N-1, -1, -1):
        if data_b[i] != sol[i]:
            ed_b = i + 1
            for j in range(i-1, -1, -1):
                if data_b[j] == sol[i]:
                    st_b = j + 1
                    return st_b, ed_b
    if st_b == None and ed_b == None:
        return 1, 1

def check(cnt, data, ans_c):
    if cnt > 1:  # 2뎁스 끝냈으면
        if data == sol:
            return ans_c
        else:
            return False
    for i in range(2):
        if i == 0:
            st_c, ed_c = front_find(data)
        else:
            st_c, ed_c = back_find(data)
        success = check(cnt + 1, swap(data, st_c, ed_c), ans_c + [(st_c, ed_c)])
        if success:  # 원본배열 성공사례 있으면 스왑기록 리턴
            return success

N = int(input())
task = list(map(int, input().split()))
sol = [i for i in range(1, N+1)]
"""
3번부터는 좌우 탐색만으로 답이 안나오는 경우가 생김.
그래서 첫 단계로 bfs를 시도> 메모리초과, dfs > 시간초과
브루트포스로 첫 단계 다 구할 필요 없음. 구간별 뒤집기이니 좌우 증감1인 구간들이 생김.
그 구간들 좌우 기준으로만 바꿔주면 됨. 한 구간 내에서는 뒤집을 필요x
"""
group = []  # 증감구간 넣을 리스트
st = 0
tmp_dir = 0
ed = 1
while True:
    if ed > N - 1:  # 인덱스 초과면 그룹에 넣기
        group.append((st + 1, ed))
        break
    if task[ed] == task[ed - 1] + 1:  # 증가구간이면
        if tmp_dir == -1:  # 이전에 감소구간이었으면 구간 전환.
            group.append((st + 1, ed + 1))
            st = ed
        tmp_dir = 1  # 증가구간 표시
        ed += 1
    elif task[ed] == task[ed - 1] - 1:  # 감소구간이면
        if tmp_dir == 1:
            group.append((st + 1, ed + 1))
            st = ed
        tmp_dir = -1
        ed += 1
    else:  # 증가도 감소도 아니면(증감 2 이상) 구간전환.
        group.append((st + 1, ed))
        st = ed
        ed += 1
        tmp_dir = 0
succeed = 0
for i4 in range(len(group)):
    if succeed:  # 아래 성공사례 나온 후 바깥 for문 깨기 위한 break
        break
    for j4 in range(i4, len(group)):
        # 시작을 i4로 해야함. 그래야 한 구간 내에서 뒤집기 가능.
        tmp = swap(task, group[i4][0], group[j4][1])  # 한 차례 뒤집은 사례
        ans = check(0, tmp, [(group[i4][0], group[j4][1])])  # 2번 더 뒤집고 원본이 나오는가?
        if ans:  # 원본이 나왔다!
            for an in ans:  # 스왑기록 순서대로 출력
                print(*an)
                succeed = 1
            break
