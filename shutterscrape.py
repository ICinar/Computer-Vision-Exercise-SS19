from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib.request
import os
from tkinter.filedialog import askdirectory
import time

def imagescrape():
    try:
        driver = webdriver.Chrome('/home/ibo/Desktop/CV/computer-vision-freie-aufgabe/chromedriver')
        driver.maximize_window()
        for i in range(1, searchPage + 1):
            url = "https://www.shutterstock.com/search?searchterm=" + searchTerm + "&sort=popular&image_type=all&search_source=base_landing_page&language=en&page=" + str(i)
            driver.get(url)
            data = driver.execute_script("return document.documentElement.outerHTML")
            print("Page " + str(i))
            scraper = BeautifulSoup(data, "lxml")
            img_container = scraper.find_all("div", {"class":"z_g_b"})
            for j in range(0, len(img_container)-1):
                img_array = img_container[j].find_all("img")
                img_src = img_array[0].get("src")
                name = img_src.rsplit("/", 1)[-1]
                try:
                    urllib.request.urlretrieve(img_src, os.path.join(scrape_directory, os.path.basename(img_src)))
                    print("Scraped " + name)
                except Exception as e:
                    print(e)
        driver.close()
    except Exception as e:
        print(e)

print("ShutterScrape v1.1")

#scrape_directory = "C:/Users/[username]/[path]"

while True:
    while True:
        print("Please select a directory to save your scraped files.")
        scrape_directory = askdirectory()
        if scrape_directory == None or scrape_directory == "":
            print("You must select a directory to save your scraped files.")
            continue
        break
    while True:
        searchCount = int(input("Number of search terms: "))
        if searchCount < 1:
            print("You must have at least one search term.")
            continue
        elif searchCount == 1:
            searchTerm = input("Search term: ")
        else:
            searchTerm = input("Search term 1: ")
            for i in range (1, searchCount):
                searchTermPart = input("Search term " + str(i + 1) + ": ")
                searchTerm += "+" + searchTermPart
        break
    while True:
        searchPage = int(input("Number of pages to scrape: "))
        if searchPage < 1:
            print("You must have scrape at least one page.")
            continue
        break
    imagescrape()
    print("Scraping complete.")
    restartScrape = input("Keep scraping? ('y' for yes or 'n' for no) ")
    if restartScrape == "n":
        print("Scraping ended.")
        break