from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

# The URL of the main page to scrape
url = 'https://www.classcentral.com/'

# A set to store all unique links we encounter
links = set()

# A counter to keep track of how many pages we've scraped
num_pages = 0

# Create a ChromeDriver instance with options to ignore certificate errors
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

# A function to scrape a single page and all the links on that page
def scrape_page(url):
    global num_pages
    # Load the page using Selenium
    driver.get(url)

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Save the HTML to a file
    filename = url.replace('/', '_').replace(':', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    num_pages += 1
    print(f'Scraped page {num_pages}: {url}')

    # Find all links on the page
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None:
            # If the link is relative, join it with the base URL
            href = urljoin(url, href)
            # If the link is on the same domain and hasn't been visited yet, add it to the set of links
            if href.startswith(url) and href not in links:
                links.add(href)
                print(href)

# Create a directory to store the scraped HTML files
directory = 'scraped_pages'
if not os.path.exists(directory):
    os.makedirs(directory)

# Change to the directory
os.chdir(directory)

# Scrape the main page and all links on that page
scrape_page(url)
for link in links.copy():
    scrape_page(link)

# Quit the ChromeDriver instance
driver.quit()

# Print the total number of pages scraped
print(f'Total pages scraped: {num_pages}')
