from Utils.boj_judge_utils import run_judge


inputdatas = [
    {"data": """6 6
1 5
3 4
5 4
4 2
4 6
5 2""", "answer": """1"""},
    {"data": """6 7
1 3
1 5
3 4
5 4
4 2
4 6
5 2""", "answer": """2"""},
    {"data": """6 3
1 2
2 3
4 5""", "answer": """0"""}
]

run_judge(inputdatas)
