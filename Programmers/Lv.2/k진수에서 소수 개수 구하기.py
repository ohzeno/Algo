# https://school.programmers.co.kr/learn/courses/30/lessons/17678
def solution(n, k):
    s = ''
    # k진수로 바꾸기.
    while n != 0:  # n이 0이 되면 끝이다.
        tmp_na = n % k  # 나머지를 뒤에 붙여주고
        s = str(tmp_na) + s
        n //= k  # 몫을 n으로
    cases = s.split('0')  # 케이스 모으기
    prime_set = set()  # 검사한 소수 다시 체크하지 않도록 세트에 저장
    ans = 0
    for case in cases:  # 각 케이스 검사
        if case == '1' or case == '':  # 1이나 공백은 패스
            continue
        elif case == '2':  # 2는 range에서 (2, 2) 돼서 걸러지니 미리 체크
            ans += 1
            continue
        case = int(case)
        if case in prime_set:  # 이미 체크했으면 개수 +1
            ans += 1
        else:  # 체크 안했으면 제곱근까지 체크하고 기록
            for i in range(2, int(case**0.5) + 1):
                if case % i == 0:
                    break
            else:
                ans += 1
                prime_set.add(case)
    return ans

inputdatas = [
    [437674, 3],
    [110011, 10],
    [12, 10]
]

"""
2022 카카오 공채 기출. Lv.2이지만 54분이나 걸렸다.
처음에는 0P0, P0, 0P, P 케이스, P에는 0이 포함되지 않는다는 점 등의 조건으로 혼란스러웠다.
문제의 조건대로 각 케이스를 따라가며 파싱하려고 했으나 좋은 방법이 떠오르지 않았다.
소수가 겹쳐져(ex_ 3과 7이 이어져 37로) 있으면 개수를 어떻게 처리해야하는가를 고민했다.
해당 케이스의 조건이 나와있지 않다고 생각하며 문제를 계속 다시 읽다보니
모든 케이스가 결국 P라는 것을 알게됐다. 그래서 0을 기준으로 split하였으나 오류가 발생했다.
00 등의 경우 0 사이가 None타입으로 요소로 들어간 것이다. 
그런 경우를 처리해주니 1번 테케에서 시간초과가 발생했다.
while문이 있었기에 조건들을 보며 테스트 해보았으나 while에서 루프에 갇힐 이유가 없었다.
그렇다면 for문으로 소수 판별하는 부분이 문제란 것인데
이전에 소수찾기를 한 경험을 바탕으로 range(2, num//2 + 1)를 사용하여 절반만 체크하고 있었다.
여기는 해결하지 못하여 사이트의 질문들을 찾아봤고, 
제곱근까지만 체크하면 시간초과가 해결된다는 것을 알게됐다.
원리가 이해되지 않아 구글링을 하여 원리를 파악했다. 
약수의 곱으로 표현할 때, 
제곱근*제곱근을 중심으로 대칭이 되기에 뒤쪽은 체크할 이유가 없었던 것이다.
ex) 4*9  6*6  9*4
"""
for t in inputdatas:
    print(solution(t[0], t[1]))
