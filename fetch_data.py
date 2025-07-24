import requests

# Replace with your actual file URL (direct download link)
url = 'https://raw.githubusercontent.com/cybersample/objective-see/refs/heads/main/atomicStealer2_valid.json'
output = 'data/downloaded_file.json'

response = requests.get(url)
with open(output, 'wb') as f:
    f.write(response.content)