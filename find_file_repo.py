import os
import sys
import subprocess

def find_file_in_repo(root_dir, filename):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            # This directory is a Git repository
            repo_path = os.path.abspath(dirpath)
            print(f"Searching in repository: {repo_path}")
            try:
                # Use git ls-tree to check if the file exists in the repository
                result = subprocess.run(['git', 'ls-tree', '--name-only', '-r', 'HEAD', filename], 
                                        cwd=repo_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
                if result.returncode == 0 and result.stdout:
                    print(f"File '{filename}' found in repository: {repo_path}")
                elif result.returncode != 0:
                    print(f"Error running git ls-tree: {result.stderr.decode('utf-8').strip()}")
            except subprocess.CalledProcessError as e:
                print(f"Error running git ls-tree: {e}")
                continue

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 find_file_repo.py FILENAME")
        sys.exit(1)
    
    filename = sys.argv[1]
    root_directory = '.'  # You can change this to the root directory you want to search from
    
    find_file_in_repo(root_directory, filename)
