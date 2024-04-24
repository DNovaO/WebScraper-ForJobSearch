from bs4 import BeautifulSoup
from urllib.request import urlopen

""" 

    BeatifulSoup it's a powerful parser library, that may help us 
    getting all the HTML, parsing out HTML pages. instead of using
    Regex we can use a HTML parser as below.

"""

"""
    HTML parsers like Beautiful Soup can save you a lot of time and 
    effort when it comes to locating specific data in web pages. 
    that even a sophisticated parser like Beautiful Soup can't 
    interpret the HTML tags properly.

"""

url = "http://olympus.realpython.org/profiles/dionysus"
# Open the URL and read the HTML content
page = urlopen(url)
html = page.read().decode("utf-8")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Print the text content of the page
print(soup.get_text())

# Find all <img> tags in the HTML content
print(soup.find_all("img"))

# Find the first and second <img> tags
image1, image2 = soup.findAll("img")

# Print the tag name of the first image
print(image1.name)

# Print the 'src' attribute of both images
print(image1["src"])
print(image2["src"])

# Print the <title> tag of the page
print(soup.title)

# Print the string inside the <title> tag
print(soup.title.string)