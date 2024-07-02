import csv
import networkx as nx
import matplotlib.pyplot as plt

# 读取CSV文件
input_csv = 'functions_with_calls.csv'
output_image = 'function_call_graph.png'

# 创建一个有向图
G = nx.DiGraph()

# 读取CSV并添加节点和边
with open(input_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # 跳过标题行
    for row in reader:
        if len(row) < 5:
            print(f"Skipping row with insufficient columns: {row}")
            continue  # 确保有足够的列

        class_name = row[0].strip()
        function_name = row[3].strip()
        calling_functions = row[4].strip().split()

        print(f"Class: {class_name}, Function: {function_name}, Called By: {calling_functions}")

        for calling_function in calling_functions:
            if calling_function:  # 确保不是空字符串
                G.add_edge(calling_function, f"{class_name} {function_name}")

# 检查图中是否有节点和边
print(f"Nodes: {G.nodes()}")
print(f"Edges: {G.edges()}")

# 绘制图形
plt.figure(figsize=(100, 80))

# 使用不同的布局算法
pos = nx.spring_layout(G)  # 你可以尝试 nx.circular_layout(G) 或 nx.shell_layout(G)

# 绘制节点、边和标签
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

plt.title('Function Call Graph')

# 保存图形为PNG文件
plt.savefig(output_image, format='png')

