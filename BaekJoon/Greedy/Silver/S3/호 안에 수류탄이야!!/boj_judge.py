from Utils.boj_judge_utils import run_judge


inputdatas = [
    {"data": """5
0 5 10 15 100
10 5 6 100""", "answer": """권병장님, 중대장님이 찾으십니다"""},
    {"data": """5
0 5 10 15 100
10 5 6 0""", "answer": """엄마 나 전역 늦어질 것 같아"""}
]

run_judge(inputdatas)
