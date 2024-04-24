from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup


profile_url = "https://unsplash.com/s/photos/tomato"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
# Create a request object with headers
request = Request(profile_url, headers=headers)

page = urlopen(request)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

# Find all <img> tags
images = soup.find_all("img")

# Extract and print the src attribute of each image
for img in images:
    src = img.get("src")
    if src:
        img_url = src
        print("-------------")
        print(img_url)