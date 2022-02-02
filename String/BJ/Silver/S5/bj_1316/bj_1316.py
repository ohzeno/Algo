# https://www.acmicpc.net/problem/1316
import sys

sys.stdin = open("input.txt")

n = int(input())
words = [input() for _ in range(n)]
res = []
for word in words:
    w = [word[0]]
    # 두번째 글자부터 이전 글자랑 다를 때만 체크
    for i in range(1, len(word)):
        if word[i] != w[-1]:
            # 이전 글자랑 다르고 나온 적 없는 글자면 추가
            if word[i] not in w:
                w.append(word[i])
            # 이전글자랑 다른데 나온 적 있으면 그룹단어가 아님.
            else:
                break
    # 브레이크 된 적 없거나 한글자(for문 안돌아서 else로 바로 넘어옴)인 경우 단어 추가
    else:
        res.append(word)
# 단어리스트 길이 출력
print(len(res))
