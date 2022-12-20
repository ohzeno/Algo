# https://www.acmicpc.net/problem/2630
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def check(data):
    length = len(data)
    summation = 0
    for i in range(length):
        summation += sum(data[i])
    if summation == length ** 2:
        return 'blue'
    if summation == 0:
        return 'white'
    else:
        return 0

def divide(data):
    global blue, white
    length = len(data)
    if not length == 1:
        half = length//2
        squares = []
        for i in range(2):
            for j in range(2):
                # 4등분
                tmp = [data[k][j * half: j * half + half] for k in range(i * half, i * half + half)]
                squares.append(tmp)
        for square in squares:
            # 각각 나눠야하는지 체크
            coler = check(square)
            if coler == "blue":
                blue += 1
            elif coler == "white":
                white += 1
            else:
                divide(square)

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0
first_check = check(mat)  # 나눠야하는지 체크
if first_check == "blue":
    blue += 1
elif first_check == "white":
    white += 1
else:
    divide(mat)
print(white)
print(blue)


