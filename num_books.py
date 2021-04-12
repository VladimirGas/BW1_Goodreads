BOOKS_PER_PAGE = 100

def scraper(num_books):
    pages = num_books / BOOKS_PER_PAGE
    return pages

print(scraper(75))