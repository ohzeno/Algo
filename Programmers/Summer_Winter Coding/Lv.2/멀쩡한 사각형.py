# https://school.programmers.co.kr/learn/courses/30/lessons/62048
"""
모든 칸은 1 x 1 크기의 정사각형.
누군가 이 종이를 대각선 꼭지점 2개를 잇는 방향으로 잘랐음.
온전한 사각형만 사용하려고 함.
사용할 수 있는 정사각형의 개수 리턴.
w, h는 1억 이하.
"""
from math import gcd
def solution(w,h):
    if w == h:
        return w * h - w
    elif w == 1 or h == 1:
        return 0
    return w * h - (w + h - gcd(w, h))
    # return w * h - (w + h - gcd(w, h))
    # visited = set()
    # for x in range(1, w):
    #     y = h * x / w
    #     if y == int(y):
    #         ld = (x - 1, y - 1)
    #         ru = (x, y)
    #         visited.add(ld)
    #         visited.add(ru)
    #         continue
    #     left = (x - 1, int(y))
    #     right = (x, int(y))
    #     visited.add(left)
    #     visited.add(right)
    # for y in range(1, h):
    #     x = y * w / h
    #     if x == int(x):
    #         ld = (x - 1, y - 1)
    #         ru = (x, y)
    #         visited.add(ld)
    #         visited.add(ru)
    #         continue
    #     top = (int(x), y)
    #     bottom = (int(x), y-1)
    #     visited.add(top)
    #     visited.add(bottom)
    # return w * h - len(visited)

inputdatas = [
    [5, 3]
]

"""
Summer/Winter Coding(2019) 기출. 
Lv.2. 현 시점 완료한 사람 17,410명, 정답률 43%
규칙을 찾지 못했다. 인풋 아웃풋 숫자로 규칙을 찾으려 했는데
알고보니 기하학적인 부분에서 규칙을 찾아야 했다.

선분을 체크하는 풀이를 했을 때 테케6이 계속 틀렸다고 나왔는데
알고보니 나눗셈 오차가 문제다.
그래서 
y = h / w * x를
y = h * x / w로 바꾸면 통과된다...
나눗셈을 먼저하면 오차가 생긴 채로 곱셈이 되므로 
나눗셈을 나중에 하면 오차가 줄어든다.

공식 증명이 궁금해서 찾아봤는데
한국 블로거들은 그냥 공식 가져와서 쓰거나
케이스에 공식 들어맞죠? 증명 완료!
혹은 증명이라면서 문장 필수성분 다 빼고 
용어들 오용(덕분에 문맥으로 추론도 못하겠다)하면서 자신만 읽을 수 있는 글을 적어뒀다.
페터 빅셀의 '책상은 책상이다'도 아니고...

그걸 또 사람들은 와! 증명이다! 이러고 있고.
좀 답답해서 md파일을 따로 만들어서 증명을 적어둔다.

공식을 증명해서 푼 사람은 없거나, 있어도 글을 남기지 않은 듯 하다.
정답률 43%인 이유는 당연히 그냥 블로그 풀이 퍼온 사람들 때문인듯.
"""

for t in inputdatas:
    print(solution(*t))