import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import sys

def read_csv(file_name):
    # Read the CSV file
    df = pd.read_csv(file_name, header=None, names=['Function', 'File', 'CalledBy'])
    df['CalledBy'] = df['CalledBy'].apply(lambda x: x.split() if pd.notna(x) else [])
    return df

def build_graph(df):
    # Build a directed graph from the DataFrame
    G = nx.DiGraph()
    for _, row in df.iterrows():
        function = row['Function'].strip()
        for caller in row['CalledBy']:
            G.add_edge(caller.strip(), function)
    return G

def traverse_graph(G, start_function, max_depth):
    # Perform BFS to traverse the graph up to max_depth
    visited = set()
    queue = [(start_function, 0)]
    result = []

    while queue:
        current_function, current_depth = queue.pop(0)
        if current_depth > max_depth:
            continue
        if current_function not in visited:
            visited.add(current_function)
            result.append((current_function, current_depth))
            for caller in G.predecessors(current_function):
                queue.append((caller, current_depth + 1))

    return result

def plot_call_graph(G, traversal_result, output_file):
    subgraph_nodes = [node for node, _ in traversal_result]
    subgraph = G.subgraph(subgraph_nodes)
    
    pos = nx.spring_layout(subgraph)
    plt.figure(figsize=(12, 8))
    nx.draw(subgraph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10, font_weight='bold')
    plt.title(f"Call Graph (up to specified depth)")
    plt.savefig(output_file)
    plt.close()

def main():
    if len(sys.argv) != 4:
        print("Usage: python callerGraph.py function_name N outputFileName.png")
        sys.exit(1)

    start_function = sys.argv[1].strip()
    max_depth = int(sys.argv[2])
    output_file = sys.argv[3]

    # Read the CSV and build the graph
    df = read_csv("functions_with_calls.csv")
    G = build_graph(df)

    if start_function not in G.nodes:
        print(f"Function {start_function} not found in the graph.")
        sys.exit(1)

    # Traverse the graph
    traversal_result = traverse_graph(G, start_function, max_depth)

    # Plot the call graph
    plot_call_graph(G, traversal_result, output_file)
    print(f"Call graph saved to {output_file}")

if __name__ == "__main__":
    main()
