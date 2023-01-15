# https://www.acmicpc.net/problem/21921
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

# x일 동안 가장 많이 들어온 방문자 수, 그 기간이 몇 개인가?
n, x = map(int, input().split())
datas = list(map(int, input().split()))
acc = [0] * (n - x + 1)  # 각 인덱스를 시작으로 x일 동안 방문자 수
acc[0] = sum(datas[:x])
for i in range(1, n - x + 1):
    # 이전 방문자 수에서 범위 제외된 인원 제거, 새로 들어온 인원 추가
    acc[i] = acc[i - 1] - datas[i - 1] + datas[i + x - 1]
max_visiter = max(acc)
if max_visiter:
    print(max_visiter)
    print(acc.count(max_visiter))
else:
    print('SAD')


"""
현 시점 S3. 제출 3703 정답률 39.598 %
모든 예제 테케 굳이 테스트해보고 제출, 정답처리까지 8분 30초 걸렸다.
투포인터 문제라고 해서 들어왔는데 범위가 고정이라 투포인터가 아니라 슬라이딩 윈도우다.
"""