import argparse
import requests
import os

def download_file(url, local_filename=None): 
    if local_filename is None:
        # Extract the filename from the URL
        local_filename = os.path.basename(url)
    # Make a request to the URL
    with requests.get(url, stream=True) as r:
        # Check if the request was successful
        r.raise_for_status()
        # Open the local file for writing
        with open(local_filename, 'wb') as f:
            # Iterate over the content and write it to the file
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: 
                    f.write(chunk)
    return local_filename
  
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("-o", "--output", type=str, help="Name of the file to save as", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print("URL:", args.url)
print("Output Filename:", args.output)

# Call the download_file function with provided arguments
download_file(args.url, args.output)
