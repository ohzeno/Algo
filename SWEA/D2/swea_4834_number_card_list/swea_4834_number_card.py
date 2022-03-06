# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n = int(input())
    count_li = [0] * 10
    num = input()
    for i in range(n):
        count_li[int(num[i])] += 1  # 카드별 카운팅
    max_count = count_li[0]     # 최대갯수 초기화
    for j in range(10):
        if count_li[j] > max_count:
            max_count = count_li[j]  # 최대갯수 갱신
    # 가장 많은 카드에 적힌 숫자
    max_num = count_li.index(max_count)  # 최대갯수의 인덱스 = 해당 카드 종류
    count = 0   # 최대 카드 장수에 해당하는 카드종류 수
    max_idx = []
    for k in range(10):  # 인덱스로 순회
        if count_li[k] == max_count:
            count += 1
            # 최대 카드 장수에 해당하는 카드 종류 체크
            max_idx.append(k)
    if count > 1:   # 최대 카드 장수 같은 카드 여럿일 때
        max_num = max_idx[0]
        for l in max_idx:  # 가장 큰 카드 찾기
            if l > max_num:
                max_num = l
    print('#{} {} {}'.format(tc + 1, max_num, max_count))

