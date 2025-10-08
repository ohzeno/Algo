# https://www.acmicpc.net/problem/27172
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
각 플레이어는 1부터 10^6 사이의 수가 적힌 서로 다른 카드를 한 장씩 나눠 가짐.
매 턴 플레이어는 다른 플레이어와 한 번씩 결투함.
다른 플레이어 카드에 적힌 수 % 본인의 카드에 적힌 수 = 0이면 승리.
반대면 패배. 둘 다 아니면 무승부.
승리하면 1점, 패배하면 -1점, 무승부면 0점.
본인 제외한 모든 플레이어와 한 번씩 결투 하고 나면 게임 종료.
각 플레이어가 갖고 있는 카드가 주어졌을 때
게임 종료 후의 모든 플레이어의 점수를 구하라.
2 <= N <= 10^5
모든 1 <= i <= N에 대해 1 <= xi <= 10^6
모든 1 <= i < j <= N에 대해 xi != xj
즉, 어떤 수도 x에서 두 번 이상 등장하지 않음
"""
n = int(input())
cards = list(map(int, input().split()))
max_card = max(cards)
exist = set(cards)
scores = [0] * (max_card + 1)
for num in cards:
    acc = 0
    for scale in range(2, max_card // num + 1):
        scaled_num = scale * num
        if scaled_num in exist:
            acc += 1
            scores[scaled_num] -= 1
    scores[num] += acc
print(*[scores[num] for num in cards])
# scores = {}
# for num in cards:
#     scores[num] = 0
# max_num = max(cards)
# for num in cards:
#     acc = 0
#     for scale in range(2, max_num // num + 1):
#         scaled_num = scale * num
#         if scaled_num in scores:
#             acc += 1
#             scores[scaled_num] -= 1
#     scores[num] += acc
# print(*[scores[num] for num in cards])


"""
현 시점 골드 5. 제출 2565. 정답률 40.821 %
브루트포스 태그가 달려있으면서 브루트포스 사용하면 시간초과 난다.
에라토스테네스의 체처럼 배수들을 체크해나가야 하는 문제.
중복이 없기에 굳이 Counter나 dict를 만들어서 순회돌면서 체크할 필요 없고
그냥 set로 만들어서 나중에 조회를 O(1)로 할 수 있게 한다.
값이 10만까지라 그냥 리스트 길이를 10만 + 1로 두는 사람도 있다.
나는 카드 중 가장 큰 값을 구해서 리스트 길이를 제한했다.

이렇게 카드 숫자를 인덱스로 접근할 수 있게 하지 않으면
배수들의 점수를 기록하기가 힘들다.

dict를 사용할 경우 set와 배열을 dict 하나로 대체할 수 있지만
key가 추가될 때마다 메모리 추가할당 하는 과정 때문인지
set와 배열을 따로 두는 것보다 시간을 더 사용한다.
"""
