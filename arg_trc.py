import os
import sys

def find_files_with_string(target_string, search_path, file_str):
    # List to store matching file paths
    matching_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file_str in file:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if target_string in content:
                            matching_files.append(file_path)
                except IOError as e:
                    # Skip files that can't be read due to I/O error
                    print(f"Error reading {file_path}: {e}", file=sys.stderr)

    return matching_files

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 arg_trc.py <XXX> <PATH> <FILESTR>")
        sys.exit(1)

    target_string = sys.argv[1]
    search_path = sys.argv[2]
    file_str = sys.argv[3]

    matching_files = find_files_with_string(target_string, search_path, file_str)

    for file_path in matching_files:
        print(file_path)


