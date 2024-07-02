import csv
import os
import re

# 读取CSV文件
input_csv = 'doxygen_output_combined.csv'
output_csv = 'functions_with_calls.csv'

def try_open(file_path, encodings=['utf-8', 'iso-8859-1', 'windows-1252']):
    """尝试用多种编码打开文件，直到成功或所有编码都失败"""
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except (UnicodeDecodeError, ValueError):
            continue
    raise UnicodeDecodeError(f"无法使用提供的编码打开文件: {file_path}")

def get_called_functions(file_path, function_name, all_functions):
    called_functions = set()
    content = try_open(file_path)
    lines = content.splitlines()

    # 找到函数定义的位置
    function_start = None
    pattern = re.compile(r'\b' + re.escape(function_name) + r'\b')
    for i, line in enumerate(lines):
        if pattern.search(line):
            function_start = i
            break

    if function_start is not None:
        # 查找函数调用
        for line in lines[function_start:]:
            # 简单匹配函数调用的正则表达式
            matches = re.findall(r'\b(\w+)\s*\(', line)
            for match in matches:
                if match != function_name and match in all_functions:  # 排除自身调用并仅记录functions.csv中的函数
                    called_functions.add(match)

    return called_functions

# 获取functions.csv中的所有函数名称
all_functions = set()
with open(input_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        all_functions.add(row[0])

# 重新读取functions.csv以处理每一行
with open(input_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

for row in rows:
    if "function"in row:
        function_name = row[4]
        filename = row[0]
    elif "variable" in row:
        file_path= ''
        function_name = row[3]
    elif "define" in row:
        function_name = row[3]
        file_path = row[0]
    if os.path.exists(file_path):
        try:
            print(file_path+"//"+function_name)
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
