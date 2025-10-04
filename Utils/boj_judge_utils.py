import io
import sys
import traceback
from contextlib import redirect_stdout, redirect_stderr
import subprocess
import re
import inspect
from pathlib import Path


def get_result(script_path, input_data: str) -> tuple[str, str]:
    if script_path.endswith('.py'):
        return process_py_code(script_path, input_data)
    elif script_path.endswith('.js'):
        return process_js_code(script_path, input_data)


def process_py_code(script_path, input_data: str) -> tuple[str, str]:
    # 입력 스트림을 StringIO 객체로 변경
    sys.stdin = io.StringIO(input_data)
    # 출력과 에러 캡처를 위한 StringIO 객체 생성
    output = io.StringIO()
    errors = io.StringIO()

    with open(script_path, encoding="utf-8") as f:
        code_str = f.read()

    # sys.stdin = open('input.txt') 패턴을 찾아서 주석처리
    code_str = re.sub(r"sys\.stdin\s*=\s*open\(['\"]input\.txt['\"].*?\)",
                      lambda m: '# ' + m.group(0), code_str)

    code = compile(code_str, script_path, "exec")
    # 표준 출력을 output으로 변경 후 스크립트 실행
    with redirect_stdout(output), redirect_stderr(errors):
        try:
            exec(code, {"__name__": "__main__"})
        except Exception as e:
            # 예외 발생 시 traceback 정보를 에러스트림에 출력
            tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
            # 채점기가 아닌 풀이 코드의 에러만 출력
            filtered_tb_lines = [
                line for line in tb_lines if "boj_judge.py" not in line
            ]
            errors.writelines(filtered_tb_lines)
    # 출력값, 에러값을 문자열로 변환
    return output.getvalue(), errors.getvalue()


def process_js_code(script_path, input_data: str) -> tuple[str, str]:
    with open(script_path, encoding="utf-8") as f:
        code_str = f.read()

    # input_data를 JavaScript 배열 형태로 변환
    lines_array = str(input_data.split('\n'))

    # lines 변수 할당 부분을 배열로 대체
    code_str = re.sub(
        r'realCodeLines = .*?\.split\("\\n"\);',
        f'realCodeLines = {lines_array};',
        code_str
    )

    try:
        result = subprocess.run(
            ['node', '-e', code_str],
            text=True,
            capture_output=True,
            timeout=5
        )
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)


def find_script(depth=1):
    # run_judge를 호출한 스크립트의 위치 가져오기
    caller_frame = inspect.stack()[depth]
    caller_path = Path(caller_frame.filename).parent

    # 시도할 경로들
    candidates = [
        caller_path.parent / 'i_pro.py',  # ../i_pro.py (기본)
        caller_path / f'{caller_path.name}.py',  # 백준폴더에서. 현재폴더명.py
    ]

    for path in candidates:
        if path.exists():
            return str(path)

    raise FileNotFoundError(f"스크립트를 찾을 수 없습니다. 확인한 경로: {candidates}")


def run_judge(inputdatas):
    script_path = find_script(depth=2)
    for inputdata in inputdatas:
        data, ans = inputdata["data"], inputdata["answer"]
        output, error = get_result(script_path, data)
        output = output.rstrip()  # 개행문자 제거
        if output == ans:  # 정답과 출력값이 같으면 pass
            print("pass")
        else:  # 다르면 fail과 정답, 출력값 출력
            summary = "fail"
            print(f"\nInput: {data}")
            for label, content in [("expected:", ans), ("got:", output), ("Error:", error)]:
                if label == "Error:" and not content:
                    continue
                summary += f"\n  {label}\n"
                for line in content.splitlines():
                    summary += f"    {line}\n"
                summary = summary.rstrip()
            print(summary)