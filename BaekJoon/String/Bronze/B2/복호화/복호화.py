# https://www.acmicpc.net/problem/9046
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
가장 자주 사용된 알파벳을 출력.
여럿이라면 ? 출력
"""
for _ in range(int(input())):
    s = input()
    cnt = [0] * 26
    for c in s:
        if c.isalpha():  # 알파벳인 경우만
            cnt[ord(c) - ord('a')] += 1
    max_cnt = max(cnt)
    if cnt.count(max_cnt) > 1:
        print('?')
    else:
        print(chr(cnt.index(max_cnt) + ord('a')))

"""
max, count, index를 이용하기에 시간제한이 빡박할 수 있다.
알파벳 수가 적어서 가능한 풀이.
"""
