# https://www.acmicpc.net/problem/17106
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline()

"""
가로는 A~E, 세로는 1~5
칸은 열+행으로 표기한다
가로, 세로, 대각선 빙고만 허용
"""




"""
현 시점 플래 5. 제출 3962. 정답률 26.658%
왠지 모르겠지만 코딩 문제가 아니다.
그래서 그런지 solved.ac 풀이 목록에 안나온다...
평범한 논리문제인데 복잡하다.
일단 브루트포스라고 할 수 있다.
리트나 피트등의 시험과 비교하면 명제들이 좀 애매하긴 하다.
'이 문장은 참이다'같은 역설 문제가 들어가있고, 그걸 참이라고 해야하니
논리학 면에서는 자명한 문제는 아니다.
개발자 지망생 중에 귀류법 아는 사람이 얼마나 될 지 모르겠는데
귀류법으로 시작해야 풀 수 있다.
"""