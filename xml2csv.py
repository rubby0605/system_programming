import os
import sys
import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml_file(file_path):
    data = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        for compound in root.findall('compounddef'):
            compound_name = compound.find('compoundname').text
            for section in compound.findall('sectiondef'):
                section_kind = section.get('kind')
                for member in section.findall('memberdef'):
                    member_kind = member.get('kind')
                    member_name = member.find('name').text
                    member_type = member.find('type').text if member.find('type') is not None else 'N/A'
                    
                    data.append([compound_name, section_kind, member_kind, member_name, member_type])
    except ET.ParseError as e:
        print(f"Error parsing {file_path}: {e}")
    return data

def main(directory):
    all_data = []

    for root_dir, base, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(root_dir, base, file)
                file_data = parse_xml_file(file_path)
                all_data.extend(file_data)

    if all_data:
        df = pd.DataFrame(all_data, columns=['Compound', 'Section', 'Member Kind', 'Member Name', 'Member Type'])
        df.to_csv('doxygen_output_combined.csv', index=True)
        print(f"CSV file 'doxygen_output_combined.csv' created successfully.")
    else:
        print("No valid XML data found to convert to CSV.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 xml2csv.py PATH")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"The path {directory} does not exist or is not a directory.")
        sys.exit(1)

    main(directory)

