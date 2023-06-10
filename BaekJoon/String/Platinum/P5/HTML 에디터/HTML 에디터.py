# https://www.acmicpc.net/problem/4752
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
HTML 문서가 주어졌을 때, B부터 E까지 구간을 선택한다.
B부터 E까지 부분 문자열을
원래 있던 곳에서의 서식과 동일한 서식으로 만들기 위해서
부분 문자열의 앞과 뒤에 태그를 추가해야 한다.
모든 태그는 여는 태그 <b>와 닫는 태그 </b>로 구성되어 있다. 
여는 태그와 닫는 태그는 항상 쌍으로 주어진다.
두 태그 사이에 또다른 태그를 넣을 수 있다.
내부에 아직 닫히지 않은 태그가 있다면, 최외곽 태그를 닫을 수 없다.
예를 들어, <i>abc<b>def</i>ghi</b>는 올바르지 않은 HTML이다. 
또한, 닫히지 않은 채로 같은 태그를 또 열 수 없다.
예를 들어, <b><b>recursive b</b><b/>는 올바르지 않은 HTML이다.

각 케이스는 한 줄로 이루어져 있고, B E TEXT와 같은 형식이다.
B는 선택 구간 시작, E는 선택 구간 끝, TEXT는 선택 구간에 들어갈 HTML이다. 
0 <= B <= E <= TEXT의 길이 <= 200
마지막 테스트 케이스 다음 줄에는 -1 -1이 주어진다.
TEXT는 아스키 값이 32 이상 126 이하인 문자로만 이루어져 있다.
여는 태그는 항상 "<X>"와 같은 꼴이고, X는 적어도 1글자 이상이다.
또한, 'a'~'z', 'A'~'Z', '0'~'9', '-'로만 이루어져 있다. '<'는 항상 태그에서만 사용한다.

입력으로 주어지는 HTML 문서는 항상 올바르다. 
즉, 여는 태그는 항상 그에 상응하는 닫는 태그가 있고, 모든 닫는 태그도 마찬가지이다. 
부분 문자열이 태그를 중간에 끊는 경우는 없다. 
(예를 들어, <B>로 시작하는 문자열이 있을 때, B에서부터 시작하는 부분 문자열)

각 입력에 대해서, B부터 E까지 부분 문자열을(E는 부분 문자열에 포함되지 않는다) 
원래 위치에서와 동일한 서식으로 만들기 위해 
추가해야 하는 태그를 앞과 뒤에 적절히 추가한 뒤 출력한다.
"""
def get_tag(text, i, limit):
    for j in range(i+2, limit):
        if text[j] == '>':
            tag = text[i+1:j]
            return tag, j+1

while True:
    text = input()
    if text == "-1 -1":
        break
    a, b, *_ = text.split()
    st, ed = int(a), int(b)
    text = text[2+len(a)+len(b):]
    ans = text[st:ed]
    l_ans = ed - st
    stack, in_stack = {}, {}
    i = order = 0
    while i < st:  # 잘라낸 부분 이전까지
        if text[i] == '<':  # 태그 시작
            tag, i = get_tag(text, i, st)
            if tag[0] == '/':  # 닫는 태그면 스택에서 제거
                stack.pop(tag[1:])
            else:  # 여는 태그면 스택에 추가
                stack[tag] = {
                    'order': order,
                    'closed': False,
                }
                order += 1
        else:  # 태그가 아니면 넘어감
            i += 1
    i = 0  # 초기화
    while i < l_ans:  # 잘라낸 부분
        if ans[i] == '<':  # 태그 시작
            tag, i = get_tag(ans, i, l_ans)
            if tag[0] == '/':  # 닫는 태그면
                if tag[1:] in in_stack:  # 잘라낸 부분에 대응 태그 있으면 제거
                    in_stack.pop(tag[1:])
                else:  # 이전 부분에 대응 태그 있으면 닫음
                    stack[tag[1:]]['closed'] = True
            else:  # 여는 태그면 안쪽 스택에 추가
                in_stack[tag] = order
                order += 1
        else:
            i += 1
    in_tags = sorted(in_stack.keys(), key=lambda x: -in_stack[x])
    # 안쪽 스택에 남은 태그 닫아줌
    for tag in in_tags:
        ans += f'</{tag}>'
    tags = sorted(stack.keys(), key=lambda x: -stack[x]['order'])
    # pre에 남은 태그
    for tag in tags:
        if stack[tag]['closed']:  # 안쪽에서 닫혔으면 앞쪽에만 추가
            ans = f'<{tag}>{ans}'
        else:  # 안닫혔으면 앞뒤로 추가
            ans = f'<{tag}>{ans}</{tag}>'
    print(ans)


"""
현 시점 플래 5. 제출 200. 정답률 26.230%
설명이 부족하다. 규칙을 명확히 설명하지 않아서 어려운 문제.
규칙 제대로 말하면 실~골 문제가 아닐까 싶다.
'원래 위치에서의 서식'을 지킨다는 말에 대한 설명이 없다.
그냥 보면 잘라내는 부분 이전까지의 닫히지 않은 태그를 가져와서 닫으면 되는 것 처럼 보인다
하지만 잘라낸 텍스트에 열린태그가 있으면 우선적으로 닫아줘야 하고
이전까지 열린 태그가 잘라낸 텍스트 안에서 닫힐 수도 있다.
그리고 텍스트 내부에 공백이 있을 수 있어서 
공백을 기준으로 잘라내면 잘라내는 구간을 온전히 얻어낼 수 없다.
이런 점만 신경쓰면 쉽게 풀 수 있는 문제.

파이썬 통과자 중 내 코드가 가장 빠르다.
다른 사람들 코드를 보니 비효율을 감수하고 코드를 간소화 한 듯 하다.
"""