import os
import sys
import requests
import time

bearer_token = "eyJvcmciOiI2NDA2NTFhNTIyZmEwNTAwMDEyOWJiZTEiLCJpZCI6IjlkMGQ5NzA1ZDNjMDRhNWU4YTVhZjJkMWY2OTgxYzkwIiwiaCI6Im11cm11cjEyOCJ9"
url = "https://api.opentransportdata.swiss/ojp20"
def transmit_file_to_server(file_path):
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
    else:
        print(f'Error: Failed to transmit file to server. Status code: {response.status_code}')
    time.sleep(1)
def process_folder(folder_path):
    # Iterate over all files and subfolders in the given folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file starts with 'req_'
            if file.endswith('.req.xml'):
                file_path = os.path.join(root, file)
                transmit_file_to_server(file_path)

# Check if the folder path argument is provided
if len(sys.argv) < 2:
    print('Error: Please provide the folder path as a command-line argument.')
    sys.exit(1)

# Get the folder path from command line argument
folder_path = sys.argv[1]

# Call the function to process the folder
print(f"Updating responses on examples for folder:{folder_path}")
process_folder(folder_path)