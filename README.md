Web Scraping Homework: Mission to Mars

Background:

Build a web application that scrapes data from four different websites to gather data and high resolution images related to the Mission to Mars and displays the information in a single HTML page.

Step 1 

Scraping:

https://mars.nasa.gov/news/ website was used to get the latest news on Mars mission using python libraries:- 
BeautifulSoup, splinter, pandas in a jupyter notebook.

https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars was used to scrape the featured image of mars in full resolution. 

https://space-facts.com/mars/ to gather the facts table about Mars.

https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars to get the images of 4 hemispheres of Mars.

Step 2

Flask Application and MongoDB:

Flask:

A python script to run all of the scraping code was designed and all of the scraped data was put into one Python dictionary.

'/scrape' route which will import the Python script and call the scrape function was created.

A Root route / that will query the database and pass the mars data into HTML template was also created


MongoDB:

A new database and a new collection were created. All of the scraped data was stored in the above created database.  

HTML and BootStrap:

Finally a HTML file called 'index.html' was created that displayed all of the data in the appropriate HTML elements.

