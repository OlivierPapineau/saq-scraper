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


    def get_categories(self):
        page = requests.get(self.url)
        

    # def get_categories(self)
