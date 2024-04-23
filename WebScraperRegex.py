from urllib.request import urlopen
import re

""" As we can see, using a different URL, the HTML gets a little tricky.
    Using a regular expression can solve many problems like this.
    So we're going to solve the HTML problem with that.
"""

#Initializing the url variable. 
url = "http://olympus.realpython.org/profiles/dionysus"


#Initializing the page variable than contains the method urlopen and the parameter url early created.
page = urlopen(url)
html = page.read().decode("utf-8")

# Now we initialize our pattern variable that contains de Regex
pattern = "<title.*?>.*?</title.*?>"

# Now we look for the match results
match_result = re.search(pattern, html, re.IGNORECASE)


title = match_result.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags


print(html)
print("----------------------------")
print(title)




