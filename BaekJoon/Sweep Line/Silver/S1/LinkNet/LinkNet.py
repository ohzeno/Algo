# https://www.acmicpc.net/problem/8539
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

n = int(input())
events = []
for _ in range(n):
    a, b = map(int, input().split())
    # 정렬에서 key=lambda x: (x[0], -x[1])를 할 수도 있지만 우선순위가 정석
    events.append((a, 0, 1))
    events.append((b, 1, -1))
events.sort()
active = 0
max_active = 0
for idx, priority, event in events:
    active += event
    max_active = max(max_active, active)
print(max_active)


"""
현 시점 Silver I. 제출 21. 정답률 85.714 %
문제 지문이 개판이다.
컴퓨터는 단일 지점에 연결된다.
'사이클에서 0 ≤ a < b ≤ R 지점에 연결된 컴퓨터는 링크 번호 c , a < c < b  에 연결된 컴퓨터가 다른 컴퓨터와 데이터 전송에 참여하지 않는 경우에만 데이터를 전송할 수 있습니다'
단일 지점 연결 컴퓨터를 범위에 연결한다고 표현하는 것부터 문제고, 
범위 내의 모든 컴퓨터인지 끝점 컴퓨터인지 사이 컴퓨터인지도 없다.
맥락상 a, b가 경계인 듯 하지만 단일 컴퓨터인지 범위 내 모든 컴퓨터인지 아직 모른다.
'틱 수'가 아마 '사이클' 얘기다. 멋대로 단어를 바꿨고 용어 설명도 없다.
'완료해야 할 전송에 대한 설명'의 '설명'도 정의되지 않았다
  ->입력 설명으로 a, b가 '설명'임을 알 수 있다.

예제 시나리오를 여러 방향으로 검토해보면 (a, b)는 
a, b 두 지점에 연결된 컴퓨터 사이의 전송 얘기로 추정된다.
또한 경계가 겹치는 경우 경계의 컴퓨터는 한 사이클에 한쪽 구간에서만 전송이 가능하다.
  -> 이는 '한 사이클에서 컴퓨터는 단 하나의 전송에만 참여할 수 있다'와 예제 분석으로 도출된다.

최소한 문장 필수 성분과 중의성, 논리학 기초는 가르쳤으면 좋겠다.
엄밀한 프로그래밍 언어를 다루는 사람들이 일상언어는 추상적으로 다루고 있다.
"""
