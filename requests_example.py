# Requires requests; install with: pip install requests

import requests

response = requests.get("https://www.example.com")

print("Status Code: " + str(response.status_code))