import sys
import chardet
from lxml import etree

def parse_xml_file(xml_file):
    try:
        # Auto-detect encoding using chardet
        with open(xml_file, 'rb') as f:
            xml_data = f.read()
        encoding = chardet.detect(xml_data)['encoding']

        parser = etree.XMLParser(encoding=encoding)
        tree = etree.fromstring(xml_data, parser=parser)
        root = tree.getroottree().getroot()

        # Process your XML data here
        for codeline in root.xpath('.//codeline'):
            # Example: Accessing text content of codeline
            print(codeline.text.strip() if codeline.text else '')

            # Example: Accessing refid attribute of ref element
            for ref in codeline.xpath('.//ref'):
                refid = ref.get('refid')
                if refid:
                    print(f"Found refid: {refid}")

    except etree.XMLSyntaxError as e:
        print(f"Error parsing XML file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input.xml")
    else:
        input_xml = sys.argv[1]
        parse_xml_file(input_xml)
