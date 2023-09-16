# https://school.programmers.co.kr/learn/courses/30/lessons/49993
"""
선행스킬 순서 skill과
유저들이 만든 스킬트리가 담긴 skill_trees가 주어진다.
가능한 스킬트리 개수를 return하라.
1 <= len(skill) <= 26
skill에 중복 없음.
1 <= len(skill_trees) <= 20
2 <= len(skill_trees[i]) <= 26
원소 내에 중복없음
"""
def solution(skill, skill_trees):
    # l_skill = len(skill)
    # skill_set = set(skill)
    cnt = 0
    for tree in skill_trees:
        # idx = 0
        # for s in tree:
        #     if s not in skill_set:
        #         continue
        #     if s == skill[idx]:
        #         idx += 1
        #         if idx == l_skill:
        #             cnt += 1
        #             break
        #     else:
        #         break
        # else:
        #     cnt += 1
        user_skills = ''.join([s for s in tree if s in skill])
        if user_skills == skill[:len(user_skills)]:
            cnt += 1
    return cnt



inputdatas = [
    ["CBD", ["BACDE", "CBADF", "AECB", "BDA"]],
]

"""
Summer/Winter Coding(~2018) 기출. 
Lv.2. 현 시점 완료한 사람 20,976명, 정답률 57%
괜히 시간복잡도 공간복잡도 생각하다가 꼬였다. 27분 걸림.
순서이니 next딕셔너리를 만들어서 트리를 만들어보기도 했고
idx를 따로 두는 방식으로 작성하기도 했는데

문자열이 짧아서 그냥 for문과 리스트 컴프리헨션을 사용하는게 더 빠르다.
예전엔 내가 많이 사용하던 풀이인데 
어려운 문제들 풀다보니 쉬운 문제를 어렵게 풀려 한다...
"""

for t in inputdatas:
    print(solution(*t))
