import sys
from lxml import etree
import graphviz

def generate_graph(xml_file, output_png):
    # Parse XML file
    try:
        parser = etree.XMLParser(encoding='utf-8')
        tree = etree.parse(xml_file, parser=parser)
        root = tree.getroot()
    except etree.XMLSyntaxError as e:
        print(f"Error parsing XML file: {e}")
        return
    
    # Create a directed graph
    graph = graphviz.Digraph()

    # Function to add nodes and edges based on <codeline> elements
    def add_code_lines(parent, root):
        for codeline in root.xpath('.//codeline'):
            # Extract text content from <codeline>
            line_content = codeline.text.strip() if codeline.text else ''
            
            # Find <ref> elements within <codeline>
            refs = codeline.xpath('.//ref')
            
            # Initialize node label
            node_label = ''
            
            # Process each <ref> element
            for ref in refs:
                refid = ref.get('refid')
                if refid:
                    node_label += refid + ' '
            
            # If no <ref> elements found, use the entire line content
            if not node_label:
                node_label = line_content
            
            # Add node to the graph
            graph.node(node_label, node_label)
            
            # Connect to parent node if specified
            if parent is not None:
                graph.edge(parent, node_label)
        
    # Add code lines recursively
    add_code_lines(None, root)

    # Save the graph to a file (e.g., PNG format)
    graph.render(output_png, format='png', view=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.xml output.png")
    else:
        input_xml = sys.argv[1]
        output_png = sys.argv[2]
        generate_graph(input_xml, output_png)
