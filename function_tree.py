import os
import subprocess

def generate_ctags(directory):
    tags_file = os.path.join(directory, 'tags')
    subprocess.run(['ctags', '-R', '-f', tags_file, directory], check=True)
    return tags_file

def parse_ctags(tags_file):
    functions = {}
    with open(tags_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('!_TAG_'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            name = parts[0]
            file = parts[1]
            typ = parts[3].strip()
            if typ == 'f':  # Function
                if file not in functions:
                    functions[file] = []
                functions[file].append(name)
    return functions

def print_function_tree(functions):
    for file, funcs in functions.items():
        print(f"File: {file}")
        for func in funcs:
            print(f"  Function: {func}")
        print()

def traverse_and_process_files(directory):
    tags_file = generate_ctags(directory)
    
    if not os.path.exists(tags_file):
        print(f"Tags file not found: {tags_file}")
        return

    functions = parse_ctags(tags_file)
    print_function_tree(functions)
def find_class_function_calls(file_path):
    pattern = re.compile(r'(\w+)::(\w+)')
    results = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            matches = pattern.findall(line)
            if matches:
                for match in matches:
                    results.append((line_number, match[0], match[1]))

    return results

def print_results(results):
    for line_number, cppclass, cppfunction in results:
        print(f"Line {line_number}: {cppclass}::{cppfunction}")


if __name__ == "__main__":
    directory_path = '/home/rubylin/codes/EMSW/'  # 替换为你要遍历的目录路径
    traverse_and_process_files(directory_path)

