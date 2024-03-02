import io
import sys
import traceback
from contextlib import redirect_stdout, redirect_stderr


def get_result(input_data: str) -> tuple[str, str]:
    # 입력 스트림을 StringIO 객체로 변경
    sys.stdin = io.StringIO(input_data)
    # 출력과 에러 캡처를 위한 StringIO 객체 생성
    output = io.StringIO()
    errors = io.StringIO()

    # 스크립트 컴파일
    with open(script, encoding="utf-8") as f:
        code = compile(f.read(), script, "exec")
    # 표준 출력을 output으로 변경 후 스크립트 실행
    with redirect_stdout(output), redirect_stderr(errors):
        try:
            exec(code, {"__name__": "__main__"})
        except Exception as e:
            # 예외 발생 시 traceback 정보를 에러스트림에 출력
            tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
            # 채점기가 아닌 풀이 코드의 에러만 출력
            filtered_tb_lines = [line for line in tb_lines if "boj_judge.py" not in line]
            errors.writelines(filtered_tb_lines)
    # 출력값, 에러값을 문자열로 변환
    return output.getvalue(), errors.getvalue()


inputdatas = [
    [
        """2 1
5 10
100 100
11""",
        """10""",
    ],
    [
        """3 2
1 65
5 23
2 99
10
2""",
        """164""",
    ],
]

script = "i_pro.py"

for data, ans in inputdatas:
    output, error = get_result(data)
    output = output.rstrip()  # 개행문자 제거
    if output == ans:  # 정답과 출력값이 같으면 pass
        print("pass")
    else:  # 다르면 fail과 정답, 출력값 출력
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", output), ("Error:", error)]:
            if label == "Error:" and not content:
                continue
            summary += f"\n  {label}\n"
            for line in content.splitlines():
                summary += f"    {line}\n"
            summary = summary.rstrip()
        print(summary)
