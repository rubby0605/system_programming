import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import sys

def parse_csv(file_path):
    # 读取 CSV 文件
    df = pd.read_csv(file_path)
    return df

def build_graph(df):
    G = nx.DiGraph()  # 创建有向图
    columns = df.columns.tolist()  # 获取列名列表
    if 'Caller' not in columns or 'Callee' not in columns:
        print("Error: CSV file must contain 'Caller' and 'Callee' columns.")
        sys.exit(1)
    
    for index, row in df.iterrows():
        caller = row['Caller']
        callee = row['Callee']
        G.add_edge(caller, callee)
    return G

def draw_graph(G, output_file='function_diagram.png'):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)  # 选择布局
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
    plt.title('Function Call Diagram')
    plt.savefig(output_file)
    plt.show()

def main(file_path):
    df = parse_csv(file_path)
    G = build_graph(df)
    draw_graph(G)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 csv2diag.py PATH_TO_CSV_FILE")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)

