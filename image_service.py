import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY=os.getenv("SERPER_API_KEY")

url = "https://google.serper.dev/images"
headers = {
    "X-API-KEY": "YOUR_API_KEY",
    "Content-Type": "application/json"
}
payload = {"q": "mountain landscape", "num": 5}

response = requests.post(url, headers=headers, json=payload)
data = response.json()

# Each result includes image URL, title, source page, etc.
for item in data.get("images", []):
    print(item["imageUrl"], "-", item["title"])
