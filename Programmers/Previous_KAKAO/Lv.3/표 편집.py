# https://school.programmers.co.kr/learn/courses/30/lessons/81303
def solution(n, k, cmd):  # 좌 우만 갱신해주는 풀이
    answer = ''
    pointer = {i: [i - 1, i + 1] for i in range(n)}
    alive = [1] * n  # 삭제여부 기록
    selected = [k]  # 현재 선택된 노드
    del_stack = []  # 삭제된 노드 기록용

    def select(order):  # 선택은 포인터를 타고 이동
        dir, num = order.split()
        num = int(num)
        cnt = selected[0]
        if dir == "D":
            for i in range(num):
                cnt = pointer[cnt][1]
        else:
            for i in range(num):
                cnt = pointer[cnt][0]
        selected[0] = cnt

    def delete():
        alive[selected[0]] = 0  # 선택된 노드 삭제
        del_stack.append(selected[0])  # 삭제 기록
        pre = pointer[selected[0]][0]  # 선택된 노드의 이전 노드
        post = pointer[selected[0]][1]  # 선택된 노드의 이후 노드
        if pre > -1:  # 이전 노드가 존재하면
            pointer[pre][1] = post  # 이전 노드의 우포인터를 삭제된 노드의 우 포인터로 갱신
        if post < n:  # 이후 노드가 존재하면
            pointer[post][0] = pre  # 이후 노드의 좌포인터를 삭제된 노드의 좌포인터로 갱신
            selected[0] = post  # 이후 노드를 선택
        else:
            selected[0] = pre  # 이전 노드를 선택

    def cancel():
        recover = del_stack.pop()  # 최근 삭제된 노드
        alive[recover] = 1  # 노드 살리기
        pre = pointer[recover][0]  # 삭제됐던 노드의 이전 노드
        post = pointer[recover][1]  # 삭제됐던 노드의 이후 노드
        if pre > -1:  # 이전 노드가 존재하면 우포인터를 복구한 노드로 갱신
            pointer[pre][1] = recover
        if post < n:  # 이후 노드가 존재하면 좌포인터를 복구한 노드로 갱신
            pointer[post][0] = recover

    for order in cmd:  # 명령 순회
        if order[0] in 'DU':
            select(order)
        elif order[0] == 'C':
            delete()
        else:
            cancel()
    for i in range(n):  # 차례대로 순회하며 살아있으면 O 아니면 X 기록.
        if alive[i]:
            answer += 'O'
        else:
            answer += 'X'
    return answer


inputdatas = [
    [6, 4, ["C", "U 1", "C", "Z", "U 2", "C"]],
    [8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]],
    [8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]]
]

"""
2021 카카오 채용연계형 인턴십 기출. Lv.3.
1시간 걸려서 리스트를 이용한 초안을 작성했고, 당연히 시간초과가 발생했다. 정확성 테스트에서도 4, 21, 24, 27 케이스에서 런타임 에러가 발생했다.
딕셔너리로 포인터를 만들었을 때 시간초과에 많이 당했던 기억에 리스트를 사용한 것이었다.
80분을 더 사용하여 딕셔너리로 포인터를 만들어서 두번째 풀이를 만들었고 정확성 21, 27, 효율성 7 케이스에서 런타임 에러가 발생했다. delete에서 현재 선택된 행이 마지막 행인 경우를 처리할 때, st가 n-1인가를 확인해서 인덱스 에러가 발생했다. 행이 하나라도 삭제됐다면 st가 n-1이 아니더라도 마지막 행일 경우가 있다. 다음 자리를 가리키는 포인터를 사용해 비교하면서 해결됐다.

다른 정답 풀이들을 보면 삭제, 삽입 과정에서 해당 노드의 전후 포인터만 확인하고 교체한다. 만약 복구 규칙이 달랐다면 문제가 생긴다. (solution2가 전부 갱신, solution은 좌우만 갱신)
예를 들어 4번 노드를 삭제하고 U 1 후 3번 노드를 삭제, 4번을 복구하면 다른 풀이들은 
4번 노드의 좌 포인터가 삭제된 3을 가리키고 있고 2번 노드의 우포인터는 4번이 살아났음에도 5번을 가리키고 있다. 그 상태에서 U 2를 하면 삭제된 3을 선택하게 되고, 삭제를 실행하면 본래 삭제되어야 할 2번이 살아있다.
하지만 문제에서 복구는 마지막으로 삭제된 노드를 되살리므로 포인터가 갱신되지 않는 오류가 생기지 않는다.
호텔 방 배정에서는 내 풀이처럼 노드들을 탐색하며 포인터를 전부 갱신해준다. 이런 규칙을 처음 접하면 갱신이 필요없는 케이스라는걸 문제풀이 도중에 알기는 좀 힘들 듯 하여, 갱신과정 코딩에 시간을 많이 소모할 듯 하다.
"""
for t in inputdatas:
    print(solution(t[0], t[1], t[2]))

# 초안
def solution1(n, k, cmd):
    # 한 번에 한 줄만 선택 가능
    # U X: 선택된 행에서 x칸 위의 행 선택
    # D X: 선택된 행에서 x칸 아래의 행 선택
    # C: 현재 선택된 행을 삭제 후 바로 아래 행 선택. 단, 삭제된 행이 마지막 행이면 바로 윗 행 선택
    # Z: 가장 최근에 삭제된 행을 복구. 선택된 행은 바뀌지 않음.
    # n: 처음 표 행 개수(5~1천), k: 처음 선택된 행 위치, cmd: 수행 명령어 목록(1~1천)
    # 명령 수행 후 각 행이 삭제됐으면 X 아니면 O로 문자열로 리턴
    # 표의 범위를 벗어나는 이동은 입력으로 주어지지 않음.
    answer = []
    cur_alive = [i for i in range(n)]
    cur_len = [n]
    selected = [k]
    del_stack = []
    def select(order):
        dir, num = order.split()
        if dir == "D":
            selected[0] += int(num)
        else:
            selected[0] -= int(num)

    def delete():
        del_stack.append(cur_alive[selected[0]])
        del cur_alive[selected[0]]
        if cur_len[0] - 1 < selected[0] + 1:
            selected[0] -= 1
        cur_len[0] -= 1

    def cancel():
        recover = del_stack.pop()
        idx = len(list(filter(lambda x: x < recover, cur_alive)))
        if idx <= selected[0]:
            selected[0] += 1
        cur_alive.insert(idx, recover)
        cur_len[0] += 1

    for order in cmd:
        if order[0] in "DU":
            select(order)
        elif order[0] == 'C':
            delete()
        else:
            cancel()
    idx = 0
    for i in range(n):
        if cur_alive[idx] == i:
            answer.append("O")
            idx += 1
        else:
            answer.append('X')
    return ''.join(answer)


# while로 노드 탐색하며 갱신. 이 문제에선 좌우탐색과 같음.
def solution2(n, k, cmd):
    # 한 번에 한 줄만 선택 가능
    # U X: 선택된 행에서 x칸 위의 행 선택
    # D X: 선택된 행에서 x칸 아래의 행 선택
    # C: 현재 선택된 행을 삭제 후 바로 아래 행 선택. 단, 삭제된 행이 마지막 행이면 바로 윗 행 선택
    # Z: 가장 최근에 삭제된 행을 복구. 선택된 행은 바뀌지 않음.
    # n: 처음 표 행 개수(5~1천), k: 처음 선택된 행 위치, cmd: 수행 명령어 목록(1~1천)
    # 명령 수행 후 각 행이 삭제됐으면 X 아니면 O로 문자열로 리턴
    # 표의 범위를 벗어나는 이동은 입력으로 주어지지 않음.
    answer = ''
    pointer = {i: [i - 1, i + 1] for i in range(n)}
    alive = [1] * n
    selected = [k]
    del_stack = []
    def select(order):
        dir, num = order.split()
        num = int(num)
        cnt = selected[0]
        if dir == "D":
            for i in range(num):
                cnt = pointer[cnt][1]
        else:
            for i in range(num):
                cnt = pointer[cnt][0]
        selected[0] = cnt

    def delete():
        alive[selected[0]] = 0
        del_stack.append(selected[0])
        st = selected[0]
        lf = rt = st
        visited = [st]
        while True:
            lf = pointer[lf][0]
            if lf == -1 or alive[lf]:
                break
            visited.append(lf)
        while True:
            rt = pointer[rt][1]
            if rt == n or alive[rt]:
                break
            visited.append(rt)
        for v in visited:
            pointer[v][1] = rt
            pointer[v][0] = lf
        if lf >= 0:
            pointer[lf][1] = rt
        if rt < n:
            pointer[rt][0] = lf
        if pointer[st][1] == n:
            selected[0] = lf
        else:
            selected[0] = rt

    def cancel():
        recover = del_stack.pop()
        alive[recover] = 1
        st = recover
        cur = st
        pre = []
        while True:
            cur = pointer[cur][0]
            if cur == -1:
                break
            elif alive[cur]:
                pre.append(cur)
                break
            pre.append(cur)
        for v in pre:
            pointer[v][1] = st
        pointer[st][0] = cur
        cur = st
        post = []
        while True:
            cur = pointer[cur][1]
            if cur == n:
                break
            elif alive[cur]:
                post.append(cur)
                break
            post.append(cur)
        for v in post:
            pointer[v][0] = st
        pointer[st][1] = cur

    for order in cmd:
        if order[0] in 'DU':
            select(order)
        elif order[0] == 'C':
            delete()
        else:
            cancel()
    for i in range(n):
        if alive[i]:
            answer += 'O'
        else:
            answer += 'X'
    return answer
