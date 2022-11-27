from dataclasses import fields, dataclass

import requests
from bs4 import BeautifulSoup


@dataclass
class Article:
    quote: str
    author: str
    info_about_author: str
    tags: list


class TestSiteParser:
    HOME_URL = 'http://quotes.toscrape.com/'
    # HOME_URL = urljoin(BASE_URL,)
    PRODUCT_FIELDS = [field.name for field in fields(Article)]
    PRODUCT_OUTPUT_CSV_PATH = 'article.csv'

    def get_site_products(self) -> [Article]:
        page = requests.get(self.HOME_URL).content
        first_page_soup = BeautifulSoup(page, 'lxml')

        print('Got data from first page')
        all_products = self.get_single_page_products(first_page_soup)

        number_of_pages = self.get_number_of_pages(first_page_soup)
        for page_number in range(2, number_of_pages + 1):
            print(f'Get data from page {page_number}')
            page = requests.get(self.HOME_URL, {'page': page_number}).content
            soup = BeautifulSoup(page, 'lxml')
            all_products.extend(self.get_single_page_products(soup))

        return all_products

    @staticmethod
    def get_number_of_pages(page_soup: BeautifulSoup) -> int:
        pagination = page_soup.select_one('.pagination')
        if not pagination:
            return 1
        return int(pagination.select('li')[-2].text)

    @staticmethod
    def parse_single_product(product_soup: BeautifulSoup) -> Product:
        return Product(
            title=product_soup.select_one('.title')['title'],
            description=product_soup.select_one('.description').text,
            price=float(product_soup.select_one('.price').text.replace('$', '')),
            rating=int(product_soup.select_one('p[data-rating]')['data-rating']),
            number_of_reviews=int(product_soup.select_one('.ratings > p.pull-right').text.split(' ')[0])
        )

    def get_single_page_products(self, page_soup: BeautifulSoup) -> [Product]:
        my_products = page_soup.select('.thumbnail')
        return [self.parse_single_product(product_soup) for product_soup in my_products]

    def write_products_to_csv(self, products: [Product]):
        with open(self.PRODUCT_OUTPUT_CSV_PATH, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.PRODUCT_FIELDS)
            writer.writerows([astuple(product) for product in products])
