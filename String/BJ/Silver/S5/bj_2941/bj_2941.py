# https://www.acmicpc.net/problem/2941
import sys

sys.stdin = open("input.txt")

croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
# 제출은 for문 안쪽으로 하면 됨. 디버깅 편의를 위해 5줄 한번에 넣음
for i in range(5):
    data = input()
    l = len(data)
    cur = res = 0
    # 입력 스트링 길이 내에서
    while cur < l:
        # 두글자가 크로아티아 알파벳이면 위치 2 이동
        a = data[cur:cur+2]
        if a in croatia:
            cur += 2
        else:  # 세글자가 크로아티아 알파벳이면 위치 3이동
            b = data[cur:cur+3]
            if b == 'dz=':
                cur += 3
            # 위에 있는 알파벳 아니면 한글자임
            else:
                cur += 1
        # 모든 경우 한글자이므로 res += 1
        res += 1
    print(res)




