# https://www.acmicpc.net/problem/2505
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
bfs, dfs로 모든 경우의 수 돌면서 체크해봤으나 메모리초과.
im 스위치문제처럼 그냥 케이스 일치하지 않는 순간 보이면 바로 스왑시도 해봄.
왼쪽부터 스왑해보고 안되면 오른쪽부터 스왑해봄. 
2번 뒤집어서 성립하는 경우만 인풋에 들어오니 그러면 무조건 답에 도달함.
각 숫자위치를 손가락으로 생각하면서 뒤집어보면 잘 성립함. 
두번째 스왑은 어느쪽부터 탐색하는지 별 의미 없는 듯 해서 그냥 2번씩 같은 방향으로 탐색함.
일반적으로 생각하면 뒤집은 구간 역순으로 뒤집어줘야 하지만 꼭 그러지 않아도 성립했음.
이게 가능한 이유를 수학적으로 증명하려면 꽤 까다로울 것 같은데 초등부 올림피아드...?
"""
def swap(data, a, b):
    a -= 1
    data1 = data[:a]
    data2 = data[a:b]
    data3 = data[b:]
    return data1 + data2[::-1] + data3

def front_find(data):
    st, ed = None, None
    for i in range(N):  # 왼쪽부터 탐색
        if data[i] != sol[i]:  # 인덱스 위치의 숫자가 제자리가 아니면
            st = i + 1  # 시작 위치 기록
            for j in range(i + 1, N):
                if data[j] == sol[i]:  # 바꿀 인덱스
                    ed = j + 1  # 끝 위치 기록
                    return st, ed
    if st == None and ed == None:
        return 1, 1
    return st, ed

def back_find(data):
    st, ed = None, None
    for i in range(N-1, -1, -1):
        if data[i] != sol[i]:
            ed = i + 1
            for j in range(i, -1, -1):
                if data[j] == sol[i]:
                    st = j + 1
                    return st, ed
    if st == None and ed == None:
        return 1, 1


N = int(input())
task = input().split()
sol = [str(i) for i in range(1, N+1)]
# bfs
# que = []
# for i in range(1, N):
#     for j in range(i, N):
#         que.append((swap(task, i, j), (i, j)))
# for q in que:
#     for i in range(1, N):
#         for j in range(i, N):
#             tmp = swap(q[0], i, j)
#             if tmp == sol:
#                 print(q[1][0], q[1][1])
#                 print(i, j)
# dfs
# for i in range(1, N):
#     for j in range(i, N):
#         tmp = swap(task, i, j)
#         for i2 in range(1, N):
#             for j2 in range(i2, N):
#                 tmp2 = swap(tmp, i2, j2)
#                 if tmp2 == sol:
#                     print(i, j)
#                     print(i2, j2)
# print(*swap(swap(sol, 1, 4), 2, 6))
ans = []  # 스왑 인덱스 저장할 리스트
tmp_list = task[:]
for _ in range(2):
    st, ed = front_find(tmp_list)  # 앞쪽부터 탐색
    ans.append((st, ed))  # 인덱스 기록
    tmp_list = swap(tmp_list, st, ed)  # 스왑
if tmp_list == sol:  # 왼쪽부터 탐색하고 두번 스왑한 리스트가 정답이면
    for an in ans:  # 스왑 인덱스 순서대로 출력
        print(*an)
else:  # 왼쪽이 안되면 오른쪽 탐색
    ans = []
    tmp_list = task[:]
    for _ in range(2):
        st, ed = back_find(tmp_list)
        ans.append((st, ed))
        tmp_list = swap(tmp_list, st, ed)
    for an in ans:
        print(*an)
