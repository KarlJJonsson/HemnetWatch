from informer import Informer
from os import system
from bs4 import BeautifulSoup
from bs4 import PageElement
import requests
import os
import time

class FirstPageCrawl:
    def __init__(self, kommun, omrade):
        self.__kommun = kommun
        self.__omrade = omrade
        self.__THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        self.__MY_FILE = os.path.join(self.__THIS_FOLDER, 'links.txt')
        self.__info = Informer

    def __getAllLinks(self, URL: str):
        links = []
        front_page = requests.get(URL, timeout = 5)
        soup = BeautifulSoup(front_page.text, "html.parser")
        containers = soup.findAll("a", class_="js-listing-card-link listing-card")
        for container in containers[1:]:
            links.append(container.get("href"))
        return links

    def __createURL(self, kommun: str, omrade: str):
        base_URL = "https://www.hemnet.se/till-salu/lagenhet/"
        if not kommun: #change from mock to real value
            omrade = "" 
        URL_trail = "?by=creation&housing_form_groups[]=apartments&order=desc&preferred_sorting=true" #queries for "nyast först"
        query_URL = base_URL+kommun+omrade+URL_trail
        return query_URL

    def initializeCrawl(self):
        self.__URL = self.__createURL(self.__kommun, self.__omrade)
        print("Watching for new objects under " + self.__URL)
        self.__iteration_counter = 0

    def runCrawl(self):
        __checkedLinks = []

        with open(self.__MY_FILE, "r") as file:
            contents = file.readlines()
            for line in contents:
                __checkedLinks.append(line[:-1])
        file.close

        links = self.__getAllLinks(self.__URL)

        __results = []

        for link in links:
            if link not in __checkedLinks:
                __results.append(link)

        if len(links) > 0:
            with open(self.__MY_FILE, "w") as file:
                file.writelines("%s\n" % link for link in links)

        count = 0
        for result in __results:
            count += 1
            print(result)
        
        print(str(count) + " new objects found.")
        self.__iteration_counter += 1
        print("HemnetWatcher has ran " + str(self.__iteration_counter) + " times since last restart.")

        if __results:
            self.__info.mail(self.__info, __results, self.__kommun, self.__omrade)