# https://school.programmers.co.kr/learn/courses/30/lessons/64062
def solution(stones, k):
    if k == 1:  # k가 1이면 모든 돌을 건너야 하므로 최소값만큼 건널 수 있음.
        return min(stones)
    leng = len(stones)
    if leng == k:  # k와 leng이 같으면 하나의 돌만 밟으면 되므로 최대값만큼 건널 수 있음.
        return max(stones)
    if sorted(stones, reverse=True) == stones:
        # 역정렬된 케이스는 끝에서 가장 멀리 뛸 수 있는 돌의 값만큼 건널 수 있음.
        # 엣지케이스. 따로 처리하면 효율성 시간초과됨.
        return stones[-k]
    accs = 900000000  # 원소 최대값이 2억이니 크게 9억으로 둠. 각 구간 최대값들 중 최소값이 정답.
    i = 0  # 탐색 인덱스
    stones = [0] + stones  # 출발점은 돌이 아니므로 추가해줌.
    while i < leng + 1 - k:  # +1은 출발점. leng + 1 - k부터는 건너뛰면 됨.
        max_num = max(stones[i + 1:i + k + 1])  # 첫 돌을 제외한 최대값
        if max_num < accs:  # 최대값이 accs보다 작으면 accs 갱신.
            accs = max_num
        for i2 in range(k, 0, -1):  # list.index는 앞쪽 인덱스를 가져오므로 건너뛰기 효율이 떨어짐.
            if stones[i + i2] == max_num:  # 최대값 찾으면 바로 그 인덱스로
                i += i2
                break
    return accs

inputdatas = [
    [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3],
    [[2, 2, 4, 3, 4, 1, 4, 3, 5, 1], 3],
    [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10],
    [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 3],
    [[2, 2, 2, 2, 2], 3]
]

"""
2019 카카오 개발자 겨울 인턴십 기출. Lv.3. 
호텔 방 배정처럼 next 딕셔너리를 사용해 22분에 정확성테스트는 통과했지만 효율성은 0점이었다.
정답 코드를 만들기까지 3시간 30분을 소모했다.
정확성 테스트에 오류가 있다. k = len(stones)이면 원소 중 최댓값이 정답이지만
최솟값을 반환하더라도 정확성 테스트를 모두 통과한다.
효율성 13번 테케 때문에 무조건 이분탐색을 사용해야 한다는 말이 많았다.
실제로 넷상의 풀이는 내가 찾은 몇십 개 모두 이분탐색이었다.
나는 슬라이딩 윈도우를 사용하되, 예외 처리를 해주어서 모두 통과했다.
"""
for t in inputdatas:
    print(solution(t[0], t[1]))
