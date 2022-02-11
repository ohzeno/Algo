# https://swexpertacademy.com/main/learn/course/lectureHtmlViewer.do
import sys
sys.stdin = open('input.txt')

# tc의 수
T = int(input())

# T만큼 반복해서 로직 실행
# 근데 요렇게 하면 tc에 들어갈 값이
# 0부터 시작
# #1 일반적인 출력에제는 1분터
for tc in range(1, T+1):
    # 문제의 주어지는 값에 따라
    N = int(input())
    numbers = list(map(int, input().split()))

    # 최종 결과값
    result = 0
    # 전체 리스트 순회
    for i in range(N):
        # i번째의 최대 낙차 값은
        max_height = len(numbers) - (i+1)
        # i 다음 행부터 박스 끝까지 반복
        for j in range(i+1, len(numbers)):
            # i보다 j가 더 큰 경우,
            # 최대 낙차 - 1
            if numbers[i] <= numbers[j]:
                max_height -= 1
        if result <= max_height:
            result = max_height


    # 최종 출력은 문제에 제시된 출력 예제에 따라서 출력
    # .format 사용
    print('#{} {}'.format(tc, result))
