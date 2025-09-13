import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def search_image(image_query: str):
    SERPER_API_KEY=os.getenv("SERPER_API_KEY")

    url = "https://google.serper.dev/images"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": image_query, "num": 5} # image_query = image you want to find

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    image_list = []
    # Each result includes image URL, title, source page, etc.
    for item in data.get("images", []):
        image_list.append({
            "imageUrl": item["imageUrl"],
            "title": item["title"]
        })

    return image_list