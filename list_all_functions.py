import sys
import re, os
import subprocess

def find_all_files(all_cpp_file, PATH):
    for subdir in os.listdir(PATH):
        if os.path.isdir(PATH+'/'+subdir) is True:
            for file in os.listdir(PATH+'/'+subdir):
                i = 0
                if ".cpp" in file:
                    all_cpp_file[file] = i
                    i += 1
    return all_cpp_file
def find_class_function_calls(file_path):
    results = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):

    return results
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
def find_call_func(cpp_file, all_func, call_func, file_num):
    pattern = re.compile(r'(\w+)::(\w+)')
    if os.path.isfile(cpp_file) is False or ".cpp" not in cpp_file:
        return call_func
    print(cpp_file)
    f = open(cpp_file)
    lines = f.readlines()
    for line in lines:
        matches = pattern.findall(line)
        if matches:
            for match in matches:
                results.append((line_number, match[0], match[1]))
    return call_func

def find_class_function_calls(file_path):
    pattern = re.compile(r'(\w+)::(\w+)')
    results = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            matches = pattern.findall(line)
            if matches:
                for match in matches:
                    results.append((line_number, match[0], match[1]))
    return results = file_num
    f.close()
    return call_func
def find_all_func(all_func):
    f = open(sys.argv[2]+"/function_list.txt","r")
    lines = f.readlines()
    for line in lines:
        line1 = re.sub("[\s\S]+f,",",",line)
        mat = re.split(",", line1)
        all_func[mat[1]] = 1
    return all_func

all_cpp_file = {}
all_func = {}
call_func = {}
PATH = "./"
i = 0
all_cpp_file = find_all_files(all_cpp_file, PATH)
all_func = find_all_func(all_func)
for root, dirs, files in os.walk(PATH):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    find_call_func(file_path, all_func, call_func, i)
            except Exception as e:
                print(f"Error opening file {file_path}: {e}")
all_num = i - 1
f = open(sys.argv[2]+"function_call.txt","w", encoding='utf-8')
for i in range(all_num):
    str_use = ''
    for func in all_func.keys():
        if all_func[func] == i:
            str_use += ", " + str(func)
f.close()
