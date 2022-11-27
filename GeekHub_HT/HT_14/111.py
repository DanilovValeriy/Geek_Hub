from dataclasses import dataclass
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

CSV_PATH = 'my_parser.csv'
response = requests.get('http://quotes.toscrape.com/').content
# re
soup = BeautifulSoup(response, 'lxml')
# articles
my_articles = soup.select('.quote > .text')
# authors
my_author = soup.select('small.author')
# link to info_about_author
link_to_info_about_author = soup.select('div span a[href^="/author"]')
# for link in link_to_info_about_author:
# print(link['href'])

# link of next page
links_of_next_pages = soup.select_one('.next a')['href']
print(links_of_next_pages)


# print(my_author)


# for articles in my_author:
#     print(articles.text)


# print(my_articles)


@dataclass
class Article:
    quote: str
    author: str
    info_about_author: str
    tags: list


def get_single_page_products(self, page_soup: BeautifulSoup) -> [Article]:
    my_products = page_soup.select('.quote')
    return [self.parse_single_product(product_soup) for product_soup in my_products]


# def top_ten_tags(page) -> list:
#     finally_list = []
#     soup = BeautifulSoup(page, 'lxml')
#     my_tags = soup.select('.tag-item > [href]')
#     for el in my_tags:
#         # обережно, кров з очей. Намагався зробити через селекти, не вдалося
#         finally_list.append(str(el).split('href=')[1].split('"')[1])
#     return finally_list


# def parse_single_product(product_soup: BeautifulSoup) -> Article:
#     return Article(
#         quote=product_soup.select_one('.title')['title'],
#         author=product_soup.select_one('.description').text,
#         info_about_author=product_soup.select_one('.price').text.replace('$', ''),
#         tags=product_soup.select_one('p[data-rating]')['data-rating']
#     )


def url_generator():
    BASE_URL = 'http://quotes.toscrape.com/'
    for number in range(2, 11):
        current_url = urljoin(BASE_URL, f'/page/{number}/')
        yield current_url

# def write_products_to_csv(generator):
#     with open(CSV_PATH, 'w') as file:
#         writer = csv.writer(file)
#         for rows in generator:
#             writer.writerow(rows)

# write_products_to_csv(one_page_url())
