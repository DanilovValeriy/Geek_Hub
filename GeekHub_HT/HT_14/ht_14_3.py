'''
3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації
про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
'''
import csv
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 '
                         'Safari/537.36', 'accept': 'application/signed-exchange;v=b3;q=0.7,*/*;q=0.8'}
HOST = 'http://quotes.toscrape.com/'
FILE = 'parse.csv'


def get_html(url, params=None):
    """function get url page for parsing content"""
    response = requests.get(url, headers=HEADERS, params=params)
    if not response.ok:
        print('Something went wrong')
        return None
    return response.content


def get_author_info(link):
    FULL_URL = urljoin(HOST, link)
    soup = BeautifulSoup(get_html(FULL_URL), 'lxml')
    return soup.select_one('.author-description').text


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='quote')  # class_ must have '_'
    my_articles = []
    i = 0
    for item in items:
        info_about_author = item.select_one("div span a")["href"]
        if not info_about_author is None:
            my_articles.append({
                'article': item.select_one('.text').text,
                'author': item.select_one('small.author').text,
                'info_about_author': get_author_info(item.select_one("div span a")["href"]).strip(),
                'tags': item.select_one('.tags').text
            })
        # print(my_articles[i])
        i += 1
    return my_articles


def get_all_content():
    my_html = get_html(HOST)
    all_articles = []
    all_articles.extend(get_content(my_html))
    print('Parsed first page')
    for i in range(2, 11):
        FULL_URL = urljoin(HOST, f'/page/{i}/')
        html = get_html(FULL_URL)
        new_article = get_content(html)
        all_articles.extend(new_article)
        print(f'Parsed {i} page')
    return all_articles


def save_file(items, path):
    """Function for saving dana in csv format"""
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Article", "Author", "tags", "Info about author"])  # write lines in file
        for item in items:
            writer.writerow([item['article'], item['author'], item['tags'], item['info_about_author']])
        print('')


all_content = get_all_content()
save_file(all_content, FILE)
