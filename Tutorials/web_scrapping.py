import requests
import pandas as pd
from bs4 import BeautifulSoup

#!In this tutorial we're gonna learn how to retrieve some informations from a website

page = requests.get(
    "https://code.visualstudio.com/docs/python/tutorial-django#_explore-the-debugger")

## will connect to the page and retrieve all the html code of page
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

#*we can then search for example all the links in that html code
#print(soup.find_all("a"))##"a" refers to the <a></a> tag in html

## will find the html block code that contains id="docs-subnavbar"
find_id = soup.find(id="docs-subnavbar")
#print(find_id)
## find all li tag inside the block that contains id, will return a list of li tag
#print(find_id.find_all("li"))
#print(find_id.find_all(class_="sr-only"))

## will find the html block code that contains class="docs-subnavbar-container"
find_class = soup.find(class_="docs-subnavbar-container")
#print(find_class)
print()


## will return the fourth element of the list of li tag
#ul = find_class.find_all("ul")

li = find_class.find_all("li")
list_of_li = [lii.get_text() for lii in li]
a = find_class.find_all("a")
list_of_a = [lii.get_text() for lii in a]

#print(list_of_li)
print()
#print(list_of_a)

listt = pd.DataFrame({
    "listli": list_of_li,
    "lista": list_of_a
})
print(listt)
listt.to_csv("result.csv")
