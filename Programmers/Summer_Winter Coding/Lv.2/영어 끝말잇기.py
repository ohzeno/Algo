# https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    """
    1부터 n까지 번호가 붙은 n명의 사람이 영어 끝말잇기를 한다.
    1. 1번부터 순서대로 차례대로 단어를 말함
    2. 마지막 사람 다음 다시 1번
    3. 이전에 등장한 단어 사용x
    4. 한 글자x
    사람 수 n과 사람들이 순서대로 말한 단어 words가 매개변수로 주어질 때,
    가장 먼저 탈락하는 사람 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지
    return [번호, 차례]
    2 <= n <= 10, 2 <= len(words) <= 100
    2 <= len(단어) <= 50, 모든 단어는 알파벳 소문자
    탈락자 없으면 [0, 0] return
    """
    log = set()
    for i, word in enumerate(words):
        if word in log or (i > 0 and words[i-1][-1] != word[0]):
            return [(i%n) + 1, (i//n) + 1]
        log.add(word)
    return [0, 0]

inputdatas = [
    [3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]],
    [5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]],
    [2, ["hello", "one", "even", "never", "now", "world", "draw"]]
]

"""
Summer/Winter Coding(~2018) 기출
현 시점 Lv.2, 완료한 사람 18_641명, 정답률 70%
제약과 규칙을 옮겨적을게 많았고
차례와 주기를 정확하게 계산하는 데에 시간을 좀 써서 10분을 넘겼다.
"""

for t in inputdatas:
    print(solution(*t))
