# https://www.acmicpc.net/problem/1036
import sys

sys.stdin = open("input.txt")

a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def solve():
    N = int(input())
    count = {}
    # 0~Z 각 0인 딕셔너리
    for i in a:
        count[i] = 0
    # 주어지는 36진수 목록
    n_list = [input() for _ in range(N)]
    # 0~Z 중에 K개 고르기
    K = int(input())

    # 36진수 목록에서 하나 꺼내와서
    for num in n_list:
        for j in range(len(num)):
            # 뒤집어서 하나씩(뒤에서부터 하나씩)
            # 각 자리 십진수로 바꿔서 카운트에서 더함
            # 카운트의 A가 뒤에서 두번째라면 36**1를 더함
            # 계수만 십진수로 저장하는것
            count[num[::-1][j]] += 36 ** j

    for key in count.keys():
        # 각 카운트(계수합)에 (35(Z) - 해당 글자(36진수) 10진수값)를 곱함
        # Z로 바꿀 경우 얻을 수 있는 이득이 됨
        count[key] = count[key] * (35 - int(key, 36))

    # 리스트로 변경
    count = list(count.items())
    # 이득(x[1]) 큰 순으로(-) 정렬
    count.sort(key=lambda x: -x[1])
    # 앞에서부터 K개 선택
    for chosen in count[:K]:
        # 36진수 하나씩 가져와서 chose키값에 해당하는 글자 Z로 바꾸기
        for num in range(len(n_list)):
            n_list[num] = n_list[num].replace(chosen[0], "Z")
    # 합 넣을 변수 선언
    sum_of_num = 0

    # Z로 바꾼 36진수들 가져와서 10진수로 변환해서 합침
    for num in n_list:
        sum_of_num += int(num, 36)
    # 36진수로 바꿔서 출력
    print(to_36(sum_of_num))


def to_36(N):
    n, m = N // 36, N % 36
    # 나머지 36진수로
    M = a[m]
    # 몫이 0이 아니면 앞쪽에 재귀로 이어붙여줌
    if n != 0:
        return to_36(n) + M
    # 몫이 0이면 나머지만 보내면 끝
    else:
        return M

solve()