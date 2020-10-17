import requests
import json
from bs4 import BeautifulSoup as bSoup

URLS = {
    'en': 'https://www.saq.com/en/products',
    'fr': 'https://www.saq.com/fr/produits'
}


class Scraper:
    def __init__(self, language):
        self.site_language = language
        self.url = URLS[language]
        self.__categories = []

        self.fetch_categories()

    def fetch_categories(self):
        page = requests.get(self.url)
        soup = bSoup(page.content, 'html.parser')

        product_type_elements = soup.find_all("a", "gtm-cat-filters")

        for product in product_type_elements:
            category = product.text.strip().split('\n')[0].strip()

            href = product['href']

            self.__categories.append({
                'category': category,
                'href': href
            })

    # GETTERS / SETTERS

    def get_categories(self):
        return self.__categories
