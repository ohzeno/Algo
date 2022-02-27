# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh#none
import sys
sys.stdin = open('input.txt')

for tc in range(10):
    dmp_max = int(input())
    boxes = list(map(int, input().split()))
    dif = max(boxes) - min(boxes)
    # 평탄화가 완료된 경우 다음으로
    if dif <= 1:
        print('#{} {}'.format(tc+1, dif))
        continue
    else:
        # 평탄화 시행 조건인 동안
        while dif > 1:
            # 덤프횟수 모두 소모한 경우 브레이크
            if dmp_max < 1:
                break
            # 최고높이 하나 깎고 최저높이 하나 추가
            boxes[boxes.index(max(boxes))] -= 1
            boxes[boxes.index(min(boxes))] += 1
            # 옮겼으니 덤프횟수 깎고 높이차 갱신
            dmp_max -= 1
            dif = max(boxes) - min(boxes)
        # 평탄화 완료 혹은 덤프횟수 모두 소모
        print('#{} {}'.format(tc + 1, dif))