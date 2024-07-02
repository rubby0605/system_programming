import csv
import os
import re
import sys

# 尝试用多种编码打开文件，直到成功或所有编码都失败
def try_open(file_path, encodings=['utf-8', 'iso-8859-1', 'windows-1252']):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"无法使用提供的编码打开文件: {file_path}")

# 获取文件中的所有函数定义
def get_functions(file_path):
    functions = set()
    content = try_open(file_path)
    lines = content.splitlines()
    for line in lines:
        matches = re.findall(r'\b(\w+)\s*\(', line)
        for match in matches:
            functions.add(match)
    return functions

# 获取被调用的函数
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
            matches = re.findall(r'\b(\w+)\s*\(', line)
            for match in matches:
                if match in all_functions and match != function_name:  # 排除自身调用
                    called_functions.add(match)

    return called_functions

# 获取所有函数名称
def get_all_functions(input_csv):
    all_functions = set()
    with open(input_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            all_functions.add(row[0])
    return all_functions

# 处理CSV文件
def process_csv(input_csv, output_csv, path):
    all_functions = get_all_functions(input_csv)

    # 构建函数到文件的映射
    function_to_file = {}
    for root, dirs, files in os.walk(path):
        for file_name in files:
            if file_name.endswith('.cpp') or file_name.endswith('.h'):  # 仅处理C++源文件和头文件
                file_path = os.path.join(root, file_name)
                functions = get_functions(file_path)
                for function in functions:
                    function_to_file[function] = file_path

    with open(input_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    for row in rows:
        if len(row) < 2:
            continue  # 确保有足够的列
        function_name = row[0].strip()
        file_path = function_to_file.get(function_name)

        if file_path and os.path.exists(file_path):
            try:
                called_functions = get_called_functions(file_path, function_name, all_functions)
                # 只保留在 all_functions 集合中的函数
                called_functions = [func for func in called_functions if func in all_functions]
                row.append(' '.join(called_functions))
            except UnicodeDecodeError:
                row.append('')  # 如果无法解码文件，则添加空列
        else:
            row.append('')

    # 写回CSV文件
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 list_callee.py <input_csv> <source_code_path>")
        sys.exit(1)

    input_csv = sys.argv[1]
    source_code_path = sys.argv[2]

    output_csv = 'functions_with_calls.csv'
    process_csv(input_csv, output_csv, source_code_path)


