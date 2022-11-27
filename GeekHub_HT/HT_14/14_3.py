'''
3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації
про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
'''

# import csv
# from dataclasses import astuple, dataclass
#
# from bs4 import BeautifulSoup
#
#
# # from urllib.parse import urljoin
#
# @dataclass
# class Product:
#     title: str
#     description: str
#     price: float
#     rating: int
#     number_of_reviews: int
#
#
# class TestSiteParser:
#     BASE_URL = 'http://quotes.toscrape.com/'
#     # HOME_URL = urljoin(BASE_URL, 'test-sites/e-commerce/static/computers/laptops')
#     # PRODUCT_FIELDS = [field.name for field in fields(Product)]
#     PRODUCT_OUTPUT_CSV_PATH = 'product.csv'
#
#     @staticmethod
#     def parse_single_product(product_soup: BeautifulSoup) -> Product:
#         return Product(
#             title=product_soup.select_one('.title')['title'],
#             description=product_soup.select_one('.description').text,
#             price=float(product_soup.select_one('.price').text.replace('$', '')),
#             rating=int(product_soup.select_one('p[data-rating]')['data-rating']),
#             number_of_reviews=int(product_soup.select_one('.ratings > p.pull-right').text.split(' ')[0])
#         )
#
#     def write_products_to_csv(self, products: [Product]):
#         with open(self.PRODUCT_OUTPUT_CSV_PATH, 'w') as file:
#             writer = csv.writer(file)
#             writer.writerow(self.PRODUCT_FIELDS)
#             writer.writerows([astuple(product) for product in products])
#
#
# if __name__ == '_main_':
#     parser = TestSiteParser()
#     products = parser.get_site_products()
#     parser.write_products_to_csv(products)
