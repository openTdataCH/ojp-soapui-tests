import os
import xml.etree.ElementTree as ET
import json
from config import postman_file, output_folder, mymap
import re
import xml.dom.minidom
import random

# extracts the requests from a soapui file it also replaces the parts in mymap with the concrete values for processing
# also can do it for a postman
def fetch_journey_refs(folder_path):
    journey_refs = []

    for filename in os.listdir(folder_path):
        if filename.endswith("response.xml") and not filename.endswith(".err"):
            file_path = os.path.join(folder_path, filename)
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                namespace = "{http://www.vdv.de/ojp}"
                journey_ref = root.find(f".//{namespace}JourneyRef")
                if journey_ref is None:
                    continue
                journey_refs.append(journey_ref.text)
            except ET.ParseError:
                print(f"Error parsing XML file: {file_path}")
    if journey_refs:
        return random.choice(journey_refs)

    return "NO_VALID_JOURNEYREF"


def prettyXML(xml_string):
    # Parse the XML string into a DOM tree
    dom = xml.dom.minidom.parseString(xml_string)
    # Prettify the XML by adding indentation and line breaks
    pretty_xml = dom.toprettyxml(indent="  ")
    return pretty_xml


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
    cleaned_name = re.sub(r'[<>:"/\\|?*=]', '', name)

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

    #We need to try to find a valid JourneyRef. We do this by parsing the possible response files #TODO is a hack currently
    mymap['{ActiveJourneyRef}']=fetch_journey_refs(output_folder)

    for name, con_request_text in results.items():
        con_request_text = replace_values(con_request_text, mymap)
        con_request_text = con_request_text.replace('\r', '\n')
        con_request_text = con_request_text.replace('\n\n', '\n')
        con_request_text = con_request_text.replace('\n\n', '\n')
        filename = os.path.join(output_folder, f"case_{clean_name(name)}.req.xml")
        with open(filename, 'w',encoding='utf-8') as file:
            file.write(con_request_text)


print(mymap)

#extract_con_request(xml_file, output_folder, mymap)
extract_json_requests_postman(postman_file, mymap)
