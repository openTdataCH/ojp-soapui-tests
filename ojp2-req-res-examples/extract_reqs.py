import os
import xml.etree.ElementTree as ET
import json
from config import postman_file, output_folder, mymap
import re
# extracts the requests from a soapui file it also replaces the parts in mymap with the concrete values for processing
# also can do it for a postman
def replace_values(text, replacements):
    for old_value, new_value in replacements.items():
        text = text.replace(old_value, new_value)
    return text

def remove_duplicates(string):
    cleaned_string = re.sub(r'(\{\{)+', '{', string)
    cleaned_string = re.sub(r'(\}\})+', '}', cleaned_string)
    return cleaned_string
# Simple extractor for SOAPUI XML from file
def extract_con_request(xml_file, output_folder, mymap):
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


def clean_name(name):
    # Remove problematic characters
    cleaned_name = re.sub(r'[<>:"/\\|?*]', '', name)

    # Remove leading/trailing whitespaces and periods
    cleaned_name = cleaned_name.strip().strip('.')

    # Remove consecutive periods
    cleaned_name = re.sub(r'\.{2,}', '.', cleaned_name)
    cleaned_name.replace(" ", "")
    if len(cleaned_name) > 30:
        cleaned_name= cleaned_name[:30]
    # Ensure the name is not empty
    if not cleaned_name:
        cleaned_name = 'unnamed'

    return cleaned_name
def extract_values(results, item):
    name = item.get('name')
    if 'request' in item:
        body = item['request'].get('body', {}).get('raw')

        results[name]= remove_duplicates(body)

    if 'item' in item:
        for subitem in item['item']:
            extract_values(results,subitem)

def extract_json_requests_postman(json_file, mymap):
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    items = json_data.get('item', [])
    results = {}

    for item in items:
        extract_values(results,item)

    for name, con_request_text in results.items():
        con_request_text = replace_values(con_request_text, mymap)

        filename = os.path.join(output_folder, f"case_{clean_name(name)}.req.xml")
        with open(filename, 'w',encoding='utf-8') as file:
            file.write(con_request_text)


print(mymap)

#extract_con_request(xml_file, output_folder, mymap)
extract_json_requests_postman(postman_file, mymap)
