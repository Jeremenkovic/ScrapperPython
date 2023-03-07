# ScrapperPython


This is a Python script for web scraping using Selenium and BeautifulSoup. The script starts by importing the necessary libraries: selenium for web browsing, BeautifulSoup for parsing HTML, urllib.parse for joining URLs, and os for creating directories and files.

Then, the script sets the URL of the main page to scrape, creates an empty set to store all unique links, and initializes a counter for the number of pages scraped.

Next, the script creates a ChromeDriver instance with options to ignore certificate and SSL errors. The ChromeDriver is a WebDriver implementation that controls a Chrome browser instance programmatically.

The script defines a function scrape_page that takes a URL as input, loads the page using driver.get, parses the HTML with BeautifulSoup, saves the HTML to a file with a filename based on the URL, and finds all links on the page using soup.find_all('a'). The function checks each link to see if it is a relative link, joins it with the base URL if it is, and adds it to the set of links if it is on the same domain and hasn't been visited yet.

The script creates a directory to store the scraped HTML files, changes to the directory, and calls the scrape_page function with the main URL. Then, it loops through all the links in the set of links and calls the scrape_page function with each link.

Finally, the script quits the ChromeDriver instance and prints the total number of pages scraped.

Overall, this script provides a simple way to scrape a website and all its links recursively using Selenium and BeautifulSoup.
