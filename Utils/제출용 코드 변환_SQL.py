import clipboard

def conversion(lines):
    new_codes = []
    comm = False
    for line in lines:
        line = line.rstrip()
        if r"/*" in line or r"*/" in line:  # 여러 줄 주석 토글
            comm = not comm
            continue
        if comm:  # 여러 줄 주석은 넘어감
            continue
        if line == '' or line == '\n':  # 빈 줄
            continue
        if line.lstrip().startswith('#'):
            continue
        if line.lstrip().startswith('--'):
            continue
        if '#' in line:
            while '#' in line:
                ridx = line.rfind('#')
                if line[ridx-1:ridx+1] != "'#":
                    line = line[:line.rfind('#')].rstrip()
                else:
                    break
        if '--' in line:
            while '--' in line:
                ridx = line.rfind('--')
                if line[ridx-1:ridx+1] != "'--":
                    line = line[:line.rfind('--')].rstrip()
                else:
                    break
        line += '\n'
        new_codes.append(line)
    output = ''.join(new_codes)
    if output[-1] == '\n':
        output = output[:-1]
    return output

# 풀이 파일을 읽어서 한줄씩 리스트에 넣음.
file_path = '../sql_pro.sql'
with open(file_path, 'r', encoding='utf-8') as file:
    input_code = [line.rstrip() for line in file]
# 스키마 쿼리를 변환하고 클립보드에 복사함.
clipboard.copy(conversion(input_code))
