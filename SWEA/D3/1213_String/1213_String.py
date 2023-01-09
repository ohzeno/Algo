# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14P0c6AAUCFAYi&categoryId=AV14P0c6AAUCFAYi&categoryType=CODE&problemTitle=1213&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# UnicodeDecodeError: 'cp949' codec can't decode byte 0xe2 in position 6987: illegal multibyte sequence
# 코덱오류로 읽어오지 못해서 방식 변경
import sys
# sys.stdin = open('input.txt')
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
def input():
    return sys.stdin.readline().rstrip()

for tc in range(10):
    n = input()  # 테케 번호
    word = input()  # 찾을 문자열
    sentence = input()  # 검색할 문장
    print(f'#{n} {sentence.count(word)}')

