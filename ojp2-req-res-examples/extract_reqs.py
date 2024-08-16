import os
import xml.etree.ElementTree as ET
from config import xml_file, output_folder, mymap

# extracts the requests from a soapui file it also replaces the parts in mymap with the concrete values for processing

def replace_values(text, replacements):
    for old_value, new_value in replacements.items():
        text = text.replace(old_value, new_value)
    return text
def extract_con_request(xml_file, output_folde,mymap):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    print(root)
    con_requests = root.findall('.//{http://eviware.com/soapui/config}request')  #soapui stores the requests here

    for i, con_request in enumerate(con_requests, start=1):
        if i<2:
            continue
        con_request_text = con_request.text
        con_request_text = replace_values(con_request_text, mymap)

        filename = os.path.join(output_folder, f"case{i}.req.xml")
        with open(filename, 'w',encoding='utf-8') as file:
            file.write(con_request_text)


# Example usage

print(mymap)

extract_con_request(xml_file, output_folder,mymap)
