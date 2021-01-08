
#pip install requests

#Convert jupyter notebook to python script

#Add dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

# Set Executable Path & Initialize Chrome Browser
executable_path = {'executable_path': 'C:/Webdrivers/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)



#Scrape NASA Mars News
def marsNews():
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    html = browser.html
    soup = bs(html, "html.parser")
    try:
        article = soup.find("div", class_='list_text')
        news_title = article.find("div", class_="content_title").text
        news_p = article.find("div", class_ ="article_teaser_body").text
        output = [news_title, news_p]
    except AttributeError:
        output = ['7 Things to Know About the NASA Rover About to Land on Mars', 'The Mars 2020 Perseverance rover, which has started its approach to the Red Planet, will help answer the next logical question in Mars exploration.']
    return output
#Scrape JPL Mars Space - Featured image.
def marsImage():
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = bs(html, "html.parser")
    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    return featured_image_url

#Scrape mars facts
def marsFacts():
    import pandas as pd
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    mars_data = pd.read_html(facts_url)
    mars_data = pd.DataFrame(mars_data[0])
    mars_data.columns = ["Description", "Value"]
    mars_data = mars_data.set_index("Description")
    mars_facts = mars_data.to_html(index = True, header =True)
    return mars_facts

#scrape Mars Hemispheres
def marsHem():
    import time 
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html = browser.html
    soup = bs(html, "html.parser")
    mars_hemisphere = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=bs(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        dictionary = {"title": title, "img_url": image_url}
        mars_hemisphere.append(dictionary)
    return mars_hemisphere


#function called scrape that will execute all of your scraping code from python script
# and return one Python dictionary containing all of the scraped data.

def scrape():
    final_data = {}
    output = marsNews()
    final_data["mars_news"] = output[0]
    final_data["mars_paragraph"] = output[1]
    final_data["mars_image"] = marsImage()
    final_data["mars_facts"] = marsFacts()
    final_data["mars_hemisphere"] = marsHem()

    return final_data

