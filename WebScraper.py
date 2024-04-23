from urllib.request import urlopen

#Initializing the url variable. 
url = "http://olympus.realpython.org/profiles/aphrodite"

#Initializing the page variable than contains the method urlopen and the parameter url early created.
page = urlopen(url)

#urlopen() returns an HTTPResponse object like: <http.client.HTTPResponse object at 0x105fef820>

#object.read() returns a sequence of bytes
html_bytes = page.read()

#using objetct.decode() we can actually decode the bytes to a string using the format UTF-8
html = html_bytes.decode("utf-8")
print(html)
print("----------------")

#Extracting texts from the HTML using String Methods

# This gives the result of the index of the <title> tag, though. But we want the index of the title itself
title_index = html.find("<title>")
print(title_index)

# This gets the index of the first letter in the title.
start_index = title_index + len("<title>")
print(start_index)

# This gets the index of the closing </title> tag 
end_index = html.find("</title>")
print(end_index)

# Now we can extract the title by slicing the html string
title = html[start_index:end_index]
print(title)
