from bs4 import BeautifulSoup
import requests as re

# Going through pages
def scraper(n_pages):
    page = ''
    for i in range(1, int(n_pages) + 1):
        page = "https://www.goodreads.com/list/show/47.Best_Dystopian_and_Post_Apocalyptic_Fiction?page={}".format(i)

        # soup = BeautifulSoup(page.content, 'html.parser')
    return page

print(scraper(1))