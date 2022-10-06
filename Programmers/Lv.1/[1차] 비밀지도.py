# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    mat = []
    for i in range(n):
        tmp = ''  # 정답 문자열을 mat에 할당하기 위한 초기 문자열
        row1 = bin(arr1[i])[2:]  # 2진수로 변환 후 앞자리 0b 제거
        row2 = bin(arr2[i])[2:]
        dif1 = n - len(row1)  # 앞자리에 0 추가할 개수
        dif2 = n - len(row2)
        if dif1:
            row1 = '0' * dif1 + row1  # 앞자리에 0 추가해서 길이 n 유지
        if dif2:
            row2 = '0' * dif2 + row2
        for j in range(n):  # 해당 행의 각 열 문자열 숫자로 변환
            col1 = int(row1[j])
            col2 = int(row2[j])
            if col1 or col2:  # 둘 중 하나라도 벽이면 #으로 처리
                tmp += '#'
            else:  # 나머지는 공백으로 처리
                tmp += ' '
        mat.append(tmp)  # 만들어진 문자열 mat에 추가
    return mat

inputdatas = [
    [5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]],
    [6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]]
]
"""
2018 카카오 공채 기출.
베스트 답안은 zip, rjust, bin(i|j) 등 특이한 풀이를 한 듯 하다.
하지만 굳이 새로운 방법을 배워 트릭키하게 푸는 방법을 익히는 것 보다는
다른 문제 풀이를 연습하는게 효율적이라 판단되어 평범한 풀이만 하고 넘어간다.
14분 좀 넘게 걸렸다.
inputdatas, for문, def 세팅 후 시간이므로 아예 처음부터 작업하면 16분쯤 걸리지 않을까.
bin 함수가 익숙하지 않았고 처음에 출력조건을 제대로 안읽고 매트릭스로 풀었다가
출력이 스트링인 것을 보고 급하게 공백 스트링으로 이루어진 매트릭스를 이용하고
공백을 #으로 재할당 시도를 하는 등 시간을 좀 낭비했다.
이정도 문제는 좀 더 빨리 풀어야.
"""
for inputdata in inputdatas:
    print(solution(inputdata[0], inputdata[1], inputdata[2]))
