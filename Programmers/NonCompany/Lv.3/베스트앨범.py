# https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""
사이트에서 장르별로 가장 많이 재생된 노래를 둘씩 모아 베스트 앨범을 출시하려 한다.
노래는 고유 번호로 구분됨.
1. 많이 재생된 장르를 먼저 수록
2. 장르 내에서 많이 재생된 노래를 먼저 수록
3. 장르 내에서 재생 횟수가 같으면 고유 번호가 낮은 노래를 먼저 수록

1 <= len(genres) == len(plays) <= 10,000
장르에 곡시 하나 뿐이면 하나만 선택.
모든 장르는 재생 횟수가 다름

genres[i]는 고유번호가 i인 노래의 장르
plays[i]는 고유번호가 i인 노래의 재생 횟수
"""
from collections import defaultdict

def solution(genres, plays):
    genre_d = defaultdict(lambda: {'total': 0, 'songs': []})
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_d[genre]['total'] += play
        genre_d[genre]['songs'].append((i, play))
    genre_rank = sorted(genre_d, key=lambda x: genre_d[x]['total'], reverse=True)
    ans = []
    for genre in genre_rank:
        songs = sorted(genre_d[genre]['songs'], key=lambda x: (-x[1], x[0]))
        ans += [song[0] for song in songs[:2]]
    return ans


inputdatas = [
    {"data": [["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]], "answer": [4, 1, 3, 0]},
]

"""
해시
Lv.3. 현 시점 완료한 사람 35,642명, 정답률 53%
풀고 나서 베스트 풀이를 봤는데, 내 풀이를 더 비효율적으로 바꿔서 라인 수를 줄인 풀이였다.
"""

for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
