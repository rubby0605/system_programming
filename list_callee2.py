import csv
import os
import re
import chardet
import sys
# 读取CSV文件


input_csv = sys.argv[1]+'/functions_list0.csv'
output_csv = 'functions_with_calls.csv'
def detect_encoding(file_path):
    """检测文件编码"""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def try_open(file_path):
    """尝试用检测到的编码打开文件"""
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()

def get_called_functions(file_path, function_name, all_functions):
    called_functions = set()
    content = try_open(file_path)
    lines = content.splitlines()

    # 找到函数定义的位置
    function_start = None
    for i, line in enumerate(lines):
        if re.match(r'\b{}\b'.format(re.escape(function_name)), line):
            function_start = i
            break

    if function_start is not None:
        # 查找函数调用
        for line in lines[function_start:]:
            # 简单匹配函数调用的正则表达式
            matches = re.findall(r'\b(\w+)\s*\(', line)
            for match in matches:
                if match != function_name and match in all_functions:  # 排除自身调用并且函数在函数列表中
                    called_functions.add(match)

    return called_functions

# 获取functions.csv中的所有函数名称
all_functions = set()
with open(input_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        all_functions.add(row[0])

# 读取CSV文件并处理每一行
with open(input_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# 添加调用的函数列表到每一行
for row in rows:
    function_name = row[0]
    file_path = row[1]

    if os.path.exists(file_path):
        try:
            called_functions = get_called_functions(file_path, function_name, all_functions)
            row.append(' '.join(called_functions))
        except UnicodeDecodeError:
            row.append('')  # 如果无法解码文件，则添加空列
    else:
        row.append('')

# 写回CSV文件
with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

