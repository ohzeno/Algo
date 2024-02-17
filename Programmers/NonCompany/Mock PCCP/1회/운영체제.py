# https://school.programmers.co.kr/learn/courses/15008/lessons/121686
"""
모든 프로그램에 1~10 점수가 있다. 점수가 낮을 수록 우선순위가 높다.
각 프로그램들은 실행 시간이 정해져 있다.
준모가 만든 운영체제는 호출된 프로그램들 중 우선순위가 높은 프로그램을 먼저 실행한다.
실행 도중 더 높은 우선순위의 프로그램이 호출되어도 현재 실행중인 프로그램은 중단되지 않는다.
우선순위가 같은 프로그램들 중에서는 먼저 호출된 프로그램이 먼저 실행된다.

프로그램들의 정보를 나타내는 2차원 정수 배열 program이 주어질 때,
모든 프로그램들이 종료되는 시각과
프로그램의 점수마다 대기시간의 합을
정수 배열에 담아 return 하라.

return 해야 하는 answer 배열은 길이가 11인 정수 배열.
answer[0]은 모든 프로그램들이 종료되는 시각을 의미,
answer[i](1 ≤ i ≤ 10)는 우선순위 점수 i인 프로그램들의 대기시간 합

1 ≤ program 길이 ≤ 100,000
program[i]은 프로그램 정보, [a, b, c]의 형태.
    a는 우선순위, 1 ≤ a ≤ 10.
    b는 호출된 시각, 0 ≤ b ≤ 10,000,000
    c는 실행 시간, 1 ≤ c ≤ 1,000
    a, b쌍이 중복되는 프로그램은 입력으로 주어지지 않음.
    즉, 호출된 시각이 같으면서 점수도 같은 프로그램은 없음.
"""
from heapq import heappush as hpush, heappop as hpop


def solution(program):
    cur_t = 0
    ans = [0] * 11
    program.sort(key=lambda x: x[1], reverse=True)  # 시간 순 정렬
    q = []
    while program or q:
        if not q:  # 프로그램 없으면 t 건너뛰기
            cur_t = program[-1][1]
        else:
            # 대기큐 중 우선순위 높은 녀석을 뽑아서 실행
            # 현재 시각 이하만 넣었으니 cur_t - t하면 대기시간 나온다.
            p, st, rt = hpop(q)
            ans[p] += cur_t - st
            cur_t += rt  # 종료시각으로
        # 현재 시각 이하 프로그램 큐에 넣기
        while program and program[-1][1] <= cur_t:
            hpush(q, program.pop())
    ans[0] = cur_t
    return ans


inputdatas = [
    # [
    #     [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]],
    #     [20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0],
    # ],
    # [[[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]], [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]],
    [
        [[5, 0, 5], [1, 6, 5]],
        [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    # [
    #     [[5, 0, 5], [4, 1, 5]],
    #     [10, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
    # ],
]

"""
[PCCP 모의고사 #1] 4번 - 운영체제
lv2~3이라고들 하는데 나는 lv3~4로 느껴졌다.
처음엔 for문으로 어떻게 해보려다가 잘 안돼서 while문으로 바꿨다.
t를 1씩 증가시키는 코드를 짜고 시간초과 해결을 위해 t를 건너뛰는 것으로 바꾸면 편해진다.

다른 사람들은 오름차순 정렬하고 pop(0)을 하던데, 그러면 O(n)이라 비효율적이다.
deque를 사용하는 사람도 있지만 deque로 변환하는 과정에 O(n)이 소요된다.

그냥 나처럼 역순 정렬하고 pop() 하면 O(1)이다.
다른 사람들은 테케 11, 12에서 1초 이상 걸리는데, 나는 230ms 걸렸다.
"""

# for t in inputdatas:
#     print(solution(*t))
for data, ans in inputdatas:
    res = solution(data)
    if res == ans:
        print("pass")
    else:
        print("fail\n", f"expected:{ans}\n", f"got:{res}\n")
