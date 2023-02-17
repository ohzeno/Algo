# https://www.acmicpc.net/problem/20438
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
학생들은 접속 순서대로 3~n+2 입장번호를 받는다.
지환이가 한 명에게 출석 코드를 보내면, 그 사람은 본인 입장 번호 배수인 학생들에게 코드를 보낸다.
k명의 졸고 있는 학생들은 코드 제출도, 전달도 하지 않는다.
지환이는 무작위로 q번 출석 코드를 보낸 뒤, 특정 구간의 
입장 번호를 받은 학생 중 출석되지 않은 학생들 수를 구하고 싶다.
m개의 줄에 걸쳐 각 구간에 대해 출석되지 않은 학생 수를 출력하라.
"""
n, k, q, m = map(int, input().split())
sleep = set(map(int, input().split()))
sts = set(map(int, input().split())) - sleep
tmp = set()
for st in sts:
    for i in range(st, n + 3, st):
        if i not in sleep:
            tmp.add(i)
sts = sts.union(tmp)
accs = [0] * (n + 3)
for i in range(3, n + 3):
    if i not in sts:
        accs[i] = accs[i - 1] + 1
    else:
        accs[i] = accs[i - 1]
for _ in range(m):
    st, ed = map(int, input().split())
    print(accs[ed] - accs[st - 1])


"""
현 시점 실버2. 제출 1936.  정답률 26.518%
처음엔 매 범위가 주어질 때마다 범위를 순회하며 출석 여부를 확인했고, 시간초과 됐다.
그래서 미리 출석하지 않은 인원을 누적합으로 구해놓고 제출했으나, 또 시간초과가 발생했다.
pypy로 제출해도 시간초과가 발생했다. 도대체 어떤 방식으로 시간을 줄여야 할 지 감이 안잡혔다.
어이없게도 로직에는 문제가 없었다.
input()함수를 sys.readline().rstrip()으로 바꾸니 python3로도 통과했다.
m줄 입력을 받아야 하는데 m이 최대 5만줄이라...
백준의 시간제한이란 도대체...
"""