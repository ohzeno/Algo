# https://www.acmicpc.net/problem/1212
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
직접 한자리씩 변환했더니 pypy 써도 시간초과.
"""
# eight_num = input()
# length = len(eight_num)
# ten_num = 0
# for i in range(length):
#     ten_num += int(eight_num[i]) * 8 ** (length - i - 1)
# ans = ''
# while True:
#     ans = str(int(ten_num % 2)) + ans
#     ten_num //= 2
#     if ten_num == 1:
#         ans = str(int(ten_num)) + ans
#         break
#     elif ten_num == 0:
#         ans = 0
#         break
# print(ans)
eight_num = input()
# 8진수 > 10진수 > 2진수 후 앞의 0b 제거
print(bin(int(eight_num, 8))[2:])
