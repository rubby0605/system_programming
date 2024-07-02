import csv
import os
import re

# 读取CSV文件
input_csv = 'functions.csv'
output_csv = 'functions_with_calls.csv'

def try_open(file_path, encodings=['utf-8', 'iso-8859-1', 'windows-1252']):
    """尝试用多种编码打开文件，直到成功或所有编码都失败"""
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"无法使用提供的编码打开文件: {file_path}")

def get_called_functions(file_path, function_name):
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
                if match != function_name:  # 排除自身调用
                    called_functions.add(match)

    return called_functions

# 读取CSV文件并处理每一行
with open(input_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# 添加调用的函数列表到每一行
for row in rows:
    if len(row) < 5:
        print(f"Skipping row with insufficient columns: {row}")
        continue  # 确保有足够的列

    file_path = row[1]
    function_name = row[3]

    if os.path.exists(file_path):
        try:
            called_functions = get_called_functions(file_path, function_name)
            row.append(' '.join(called_functions))
        except UnicodeDecodeError:
            row.append('')  # 如果无法解码文件，则添加空列
    else:
        row.append('')

# 写回CSV文件
with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

