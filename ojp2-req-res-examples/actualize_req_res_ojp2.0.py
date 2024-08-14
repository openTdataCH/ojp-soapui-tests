import os
import sys
import requests
import time
from lxml import etree
import subprocess

bearer_token = "eyJvcmciOiI2NDA2NTFhNTIyZmEwNTAwMDEyOWJiZTEiLCJpZCI6IjlkMGQ5NzA1ZDNjMDRhNWU4YTVhZjJkMWY2OTgxYzkwIiwiaCI6Im11cm11cjEyOCJ9"
url = "https://api.opentransportdata.swiss/ojp20"
gitrepo ="https://github.com/VDVde/OJP"
branch ="develop"
xmlschemawriter = "."
xmlschema ="./OJP/ojp.xsd"
def download_git_repository(url, folder_path,branch):
    # Change to the target folder

    try:
        subprocess.run(['git', 'clone', '-b', branch, '--single-branch', url])
        print('Git repository downloaded successfully.')
    except subprocess.CalledProcessError:
        print('Error: Failed to download Git repository.')
def transmit_file_to_server(file_path,schema):
    # Read the contents of the file
    with open(file_path, 'rb') as file:
        file_data = file.read()
    # Set the request headers with the bearer token
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/xml'
    }
    # Transmit the file to the server
    response = requests.post(url, data=file_data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the base filename without the extension and prefix
        base_filename = os.path.splitext(os.path.basename(file_path))[0]
        base_filename = os.path.splitext(os.path.basename(base_filename))[0]

        # Construct the response file name with the base filename and '.response.xml' extension
        response_filename = f"{base_filename}.response.xml"
        # Save the response with the base filename
        response_file_path = os.path.join(os.path.dirname(file_path), response_filename)
        with open(response_file_path, 'wb') as response_file:
            response_file.write(response.content)
        print(f'Response saved as {response_file_path}')
        try:
            print("parsing file.")
            tree = etree.fromstring(response.content)
            root = tree
            print("Validation starting")
            schema.assertValid(root)
        except etree.DocumentInvalid as e:
            print("XML validation error:", e)
            tree = etree.fromstring(response.content)
            err_filename = f"{base_filename}.err.txt"
            err_file_path = os.path.join(os.path.dirname(file_path), err_filename)
            with open(err_file_path, 'w') as err_file:
                err_file.write(f"XML validation error: {e}")
        print(f'Response saved as {response_file_path}')
        print("***************************************************")

    else:
        print(f'Error: Failed to transmit file to server. Status code: {response.status_code}')
    time.sleep(1)
def process_folder(folder_path):
    print("***************************************************")
    print("schema: " + xmlschema)
    print("***************************************************")
    try:
        schema_doc = etree.parse(xmlschema)
        print("schema parsed.")
        schema = etree.XMLSchema(schema_doc)
        print("schema made ready.")
    except etree.DocumentInvalid as e:
        print("XML could not be parsed:", e)
        exit(1)
    print("***************************************************")
    # Iterate over all files and subfolders in the given folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file starts with 'req_'
            if file.endswith('.req.xml'):
                file_path = os.path.join(root, file)
                transmit_file_to_server(file_path,schema)

# Check if the folder path argument is provided
if len(sys.argv) < 2:
    print('Error: Please provide the folder path as a command-line argument.')
    sys.exit(1)

# Get the folder path from command line argument
folder_path = sys.argv[1]

# load the xsd from the repo
download_git_repository(gitrepo, xmlschemawriter, branch)

# Call the function to process the folder
print(f"Updating and validating responses on examples for folder:{folder_path}")
process_folder(folder_path)