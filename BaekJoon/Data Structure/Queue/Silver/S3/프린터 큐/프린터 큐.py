# https://www.acmicpc.net/problem/1966
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
1. 현재 큐 가장 앞 문서의 중요도 확인.
2. 나머지 문서 중 현재 문서보다 중요도가 높은 문서가 한 개라도 있으면 해당 문서 제일 뒤로 재배치.
    그렇지 않으면 바로 인쇄.
큐에 있는 문서 수, 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 출력.
중요도 중복 있을 수 있음.
"""

for _ in range(int(input())):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    q = [(pri, idx) for idx, pri in enumerate(priority)]
    cnt = 0  # 몇 번째 인쇄인가?
    while q:
        cur = q.pop(0)
        if any(cur[0] < x[0] for x in q):  # 뒤쪽에 중요도 더 높은 문서가 있으면
            q.append(cur)  # 재배치
        else:  # 없으면 인쇄
            cnt += 1
            if cur[1] == m:  # 찾는 문서면 출력 후 종료
                print(cnt)
                break


"""
현 시점 실버3. 제출 59059, 정답률 57.815%
처음엔 큐 문제지만 sorting하면 끝나는거 아닌가 싶었는데, 
중요도 중복이 있어서 큐 시뮬레이션으로 풀었다.
"""