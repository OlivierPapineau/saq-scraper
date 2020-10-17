from modules.Scraper import Scraper

LANGUAGES = ('fr', 'en')
LOCALE_TEXTS = {
    'categories': {
        'en': 'Categories',
        'fr': 'Catégories',
    }
}


class Program:
    def __init__(self):
        self.init_message = '|  SAQ Web Scraper - Olivier Papineau | 2020 Tout droits réservés'
        self.language = 'fr'
        self.category = None

        # Choosing language
        self.print_intro()
        self.choose_language()

        # Getting categories from scraper
        self.scraper = Scraper(self.language)

        # Choosing category
        self.choose_category()

    def print_intro(self):
        print('*' + '-' * (len(self.init_message) + 1) + '*')
        print(self.init_message + '  |')
        print('*' + '-' * (len(self.init_message) + 1) + '*')

    def choose_language(self):
        self.language = input(f'Choisir la langue de collecte {LANGUAGES} : ')

        if self.language not in LANGUAGES:
            print(
                f'Veuillez choisir une langue parmis les choix. {LANGUAGES}\n')
            self.choose_language()

    def choose_category(self):
        categories = list(
            map(lambda item: item['category'], self.scraper.get_categories())
        )

        print('\n')
        print(LOCALE_TEXTS['categories'][self.language] + '\n')

        for i, category in enumerate(categories):
            print(f'[{i}] {category}')


p = Program()
