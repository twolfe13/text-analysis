import pandas as pd
import numpy as np
# import seaborn as sns

# web scraping imports
from bs4 import BeautifulSoup
import requests


"""
The Beautiful Soup package is utilized to parse the html, that is, take the raw html text, and break it into Python objects. 

Note: the second argument in soup, 'lxml',  is the html parser 

"""

def define_page(url):

   

# Package the HTTP request, send the request, catch the response, and save to a variable
    r = requests.get(url)

# Extract the HTTP response as html using Requests, and save to a variable
    html = r.text

# Take the raw html text and break it into bs4 (python) objects. 
    soup = BeautifulSoup(html, 'lxml')
    
# Find and grab the table rows from the webpage, print the first 10 (print is optional). Next we loop through these, and put the 
#rows into a python list
    rows = soup.find_all('tr')
    
    list_rows = []
    
    for row in rows: 
        row_td = row.find_all('td')
        str_cells = str(row_td)
        clean_text = BeautifulSoup(str_cells,"lxml").get_text()
        list_rows.append(clean_text)
    
    #Return Python list of first 10 rows using Pandas .head() method
    df = pd.DataFrame(list_rows)

    print(df.head(10))

# Test successful creation of bs4 object
#print(type(soup))

url = 'http://www.hubertiming.com/results/2017GPTR10K'
define_page(url)

"""
optional (for testing or fun)


# Print out the title
title = soup.title
# print(title)


# Return full normal text of the webpage (simple basic webscrape)
# Removes HTML tags from bs4 object, and get webpage's text using bs4's .get_text() method, then save to a variable 
text = soup.get_text()
# print(soup.text)


# Find and grab all 'a' html tags , can print out
soup.find_all('a')
#print(soup)


# Extract and print out only hyperlinks by passing 'a' html tag (containing 'href' attribute)
all_links = soup.find_all('a')
for link in all_links:
    (link.get('href'))
#print(link)


"""


#print(rows[:10])

# This output ^ will be a list, but including the html tags again. We don't want the html tags.

# Below, we first instantiate a Python list by saving an empty list to variable: list_rows

# Now the for loop begins - first it grabs the content of all cells (cell content in html = 'td'). 
# Then it converts cell content to strings and saves to variable: str_cells
# Now that we have strings, we use bs4 get_text() bs4 method on str_cells to remove html tags. Then save to: clean_text
# To summarize,the for loop iterates through table rows and prints out (or returns) the cell content within the table rows (= 'td')




#print(row_td)

# **(repeated for learning)** convert cells to strings
#str_cells = str(row_td)

# **(repeated for learning)** clean_text = BeautifulSoup(str_cells, "lxml").get_text()

# Print cleaned text (for pure web scraping use case , not data frame)
#print(clean_text)

# Initialize Pandas data frame by passing in previously initiatilized python list called list_rows, which contain 
#normal text of the content of each table row (= 'td') on the webpage. 

