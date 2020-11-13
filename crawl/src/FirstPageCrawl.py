from os import system
from bs4 import BeautifulSoup
from bs4 import PageElement
import requests
import os
import time

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
MY_FILE = os.path.join(THIS_FOLDER, 'links.txt')

iterationCounter = 0

def getAllLinks(URL: str):
    links = []
    front_page = requests.get(URL, timeout = 5)
    soup = BeautifulSoup(front_page.text, "html.parser")
    containers = soup.findAll("a", class_="js-listing-card-link listing-card")
    for container in containers[1:]:
        links.append(container.get("href"))
    return links

def createURL(kommun: str, omrade: str):
    base_URL = "https://www.hemnet.se/till-salu/lagenhet"
    if not kommun: #change from mock to real value
        omrade = "" 
    URL_trail = "?by=creation&housing_form_groups[]=apartments&order=desc&preferred_sorting=true" #queries for "nyast först"
    query_URL = base_URL+kommun+omrade+URL_trail
    return query_URL

mock_kommun = "/taby-kommun"
mock_omrade = ""
URL = createURL(mock_kommun, mock_omrade)
print("Watching for new objects under " + URL)

while True:

    checkedLinks = []

    with open(MY_FILE, "r") as file:
        contents = file.readlines()
        for line in contents:
            checkedLinks.append(line[:-1])
    file.close

    links = getAllLinks(URL)

    results = []

    for link in links:
        if link not in checkedLinks:
            results.append(link)

    if len(links) > 0:
        with open(MY_FILE, "w") as file:
            file.writelines("%s\n" % link for link in links)

    count = 0
    for result in results:
        count += 1
        print(result)
    
    print(str(count) + " new objects found.")
    iterationCounter += 1
    print("HemnetWatcher has ran " + str(iterationCounter) + " times since last restart.")

    time.sleep(10)