import clipboard
import sys
sys.stdin = open('input.txt', encoding='utf-8')
def input():
    return sys.stdin.readline().rstrip()

def conversion(lines):
    new_codes = []
    comm = False
    for line in lines:
        line = line.rstrip()
        if "\"\"\"" in line:
            comm = not comm
            continue
        if comm:
            continue
        if line == '' or line == '\n':
            continue
        if line.strip() == "sys.stdin = open('input.txt')":
            continue
        if line.strip().startswith('#'):
            continue
        if '#' in line:
            while '#' in line:
                ridx = line.rfind('#')
                if line[ridx-1:ridx+1] != "'#":
                    line = line[:line.rfind('#')].rstrip()
                else:
                    break
        line += '\n'
        new_codes.append(line)
    output = ''.join(new_codes)
    return output

# 텍스트 파일에서 스키마 쿼리를 읽어 하나의 스트링으로 만듦.
input_code = [line for line in sys.stdin]
# 스키마 쿼리를 변환하고 클립보드에 복사함.
clipboard.copy(conversion(input_code))
