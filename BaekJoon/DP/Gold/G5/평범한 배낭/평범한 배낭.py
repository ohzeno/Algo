# https://www.acmicpc.net/problem/12865
import sys
sys.stdin = open('../../../../../input.txt')
def input():
    return sys.stdin.readline().rstrip()

# N개 물건, 무게 W, 가치 V
# 최대 K만큼 무게 넣을 수 있는 배낭
# V 합 최대로.
n, k = map(int, input().split())
# dp[i][j] = i번째 물건까지 검토할 경우 가방 제한무게가 j일 때 최적해(누적 가치)
dp = [[0] * (k + 1) for _ in range(n + 1)]
for nth in range(1, n + 1):  # n번째 물건에 대해
    tw, tv = map(int, input().split())
    for bag_w in range(1, k + 1):  # 가방 무게가 bag_w일 때 최적해
        if tw > bag_w:  # 가방 제한무게보다 무거운 건 못넣음. 이전 물건까지와 최적해가 같다.
            dp[nth][bag_w] = dp[nth - 1][bag_w]
        else:  # 넣을 가능성이 있다면
            # 이번 물건을 넣은 경우, 넣지 않은 경우 중 최적해 기록
            # 이전 물건까지 검토한 경우 중, 현 물건을 넣을 여유가 남아있는
            # 제한 무게의 기록을 가져와서 현 물건 가치를 더해준다.
            # bag_w - tw에 현 물건 넣어서 bag_w가 됨.
            dp[nth][bag_w] = max(dp[nth - 1][bag_w - tw] + tv, dp[nth - 1][bag_w])
print(dp[n][k])


"""
2023.01.06 현 시점 G5. 제출 85856, 정답률 35.281%
19분에 최초 제출. combinations로 조합 만들어서 제출했는데 시간초과였다.
dp일 것 같아서 깔끔하게 포기하고 풀이들을 찾아봤다.

대부분은 누군가가 작성해놓은 코드를 베낀 듯, 모든 풀이가 똑같았고 비효율적인 코드 부분까지 똑같았다.
(한 번만 할당하면 되는 부분을 k번 할당한다거나, 
input을 받는 순간 작업하면 되는걸 굳이 input을 미리 다 받아서 배열에 넣고 다시 순회하거나)

설명도 거의 없는데, 있더라도 주술관계가 명확하지 않아 이해하기 힘들거나
주술관계가 명확해도 설명조차 베낀 듯, 같은 내용만 적혀있고 설명이 부족하며, 이해하지 못한 것으로 보였다.
(현재 가방의 제한 무게를 '현재 가방 무게'라고 하며, 
제한 무게에서 현 물건의 무게를 빼는 이유를 작성하지 않았다. 
온갖 블로그 글들처럼 진짜 현재 가방의 무게에서 
현재 물건 무게를 빼고 현재 물건을 넣는거라면 
'무게'만 빼고 '가치'를 안뺀게 된다. 그리고 '어느 물건'을 뺐는지도 알 수 없다.
그래서 이게 논리적으로 말이 되나 혼란스러웠다.
애초에 물건 무게가 1단위로 나뉘지 않는데 '현재 가방 무게'가 1단위로 전부 존재할 수가 없다.)

풀이를 이해하고 작성한 글이라 가정하고 해석하니 비합리적인 설명들이라 혼란스러웠다.
결국 코드 자체를 살펴보며 하나하나 이해했다.
1, 2번 물건을 넣은 상태에서 1, 3번으로 바꾸는게 최적인 경우를 어떻게 기록하나 했는데
2차원 배열이기에 bag_w - tw를 통해 1번만 넣은 상태의 기록을 가져와서 3번을 넣게 된다.
최적 가치만 기록하기에 어느 물건을 넣은 기록인지는 알 수 없다.
"""