# Importing the necessary modules
import pandas as pd
import numpy as np
import time
import requests
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from htmldate import find_date
from bs4 import BeautifulSoup
from newspaper import Article

warnings.filterwarnings('ignore')

# Setting up the options for the webdriver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)


# Function for getting the news links
def get_newslinks(company, page_number):
    """For a given URL, scroll to relevant section to load appropriate HTML into driver,
    iterate through all articles on page and append article URLs to a list. Example link used
    is https://www.reuters.com/site-search/?query=META&sort=relevance&offset=20&date=past_year

    :param company: name of company to scrape articles for
    :param page_number: page number on news website to iterate over (in our case offset)

    :return: list of articles URLs
    """
    url = f"https://www.reuters.com/site-search/?query={company}&sort=relevance&offset={page_number}&date=past_year"
    driver.get(url)

    href = []

    # We use the following code to scroll down to the page
    # We do this to make sure all the elements are loaded from the page
    old_position = 0
    new_position = None

    while new_position != old_position:
        # Get old scroll position
        old_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(1)
        driver.execute_script((
            "var scrollingElement = (document.scrollingElement ||"
            " document.body);scrollingElement.scrollTop ="
            " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))

    # Making a list for appending the cleaned links
    cleaned_links = []

    # Iterate through all the articles on the page (20 articles per page)
    for article_number in range(1, 21, 1):
        try:
            article = driver.find_element('xpath',
                                          f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/ul/li[{article_number}]/div')
        except:
            print("didn't find element", end="  ")
            continue

        article_html = article.get_attribute('innerHTML')
        soup = BeautifulSoup(article_html, "lxml")

        # Getting the link
        for link in soup.find_all('a', href=True):
            partial_link = link.get('href')
            if 'https' in partial_link:
                cleaned_links.append(partial_link)
            # Some links are 'internal' to the page and don't have https in them. The web page must be appended to these links
            elif partial_link[0] == '/':
                cleaned_links.append('https://www.reuters.com' + partial_link)

    return np.unique(cleaned_links)


# Create empty list to append URLs
ticker = "META"
all_company_urls = []
for page in range(0, 900, 20):
    results = get_newslinks(ticker, page)
    all_company_urls.extend(results)

print("Collected URLS, forming dataframe")
# Create a DataFrame to populate while iterating
article_sentiments = pd.DataFrame({'ticker': [],
                                   'publish_date': [],
                                   'title': [],
                                   'body_text': [],
                                   'url': [],
                                   'price_change': []})
# Loop over all the articles
for link in all_company_urls:
    article = Article(link)
    article.download()

    try:
        article.parse()
        text = article.text
        date = find_date(link)
    except:
        print("skipped one link")
        continue

    row = {'ticker': ticker, 'publish_date': date, 'title': article.title,
           'body_text': article.text, 'url': link, 'price_change': 0}

    if all_company_urls.index(link) % 50 == 0:
        print("Completed : ", all_company_urls.index(link), " out of ", len(all_company_urls))

    article_sentiments = article_sentiments.append(pd.DataFrame(row, index=[0]))
    article_sentiments.reset_index(drop=True, inplace=True)

# Save DataFrame
article_sentiments.to_pickle("../data/" + ticker + "_article_titles.pkl")
article_sentiments.to_csv("../data/" + ticker + "_article_titles.csv", sep=',', encoding='utf-8',
                          header=True)

driver.quit()
