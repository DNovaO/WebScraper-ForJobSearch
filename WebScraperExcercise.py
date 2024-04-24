from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html = page.read().decode()

print(html)

for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)
    
print("----------------------------------------------------------------")

# Define pattern to match key-value pairs
pattern = r"([A-Za-z\s]+):\s*([A-Za-z\s]+)"

# Find all matches of key-value pairs
matches = re.findall(pattern, html, re.IGNORECASE)

# Print the extracted information
for key, value in matches:
    print(key.strip() + ":", value.strip())
    
    
print("----------------------------------------------------------------")
# Excercise
# Using Beautiful Soup, print out a list of all the links on 
# the page by looking for HTML tags with the name a and retrieving
# the value taken on by the href attribute of each tag.

profile_url = "http://olympus.realpython.org"

page = urlopen(profile_url + "/profiles")
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

print(soup)

for links in soup.findAll("a"):
    link_pages = profile_url + links["href"]
    print(link_pages)


