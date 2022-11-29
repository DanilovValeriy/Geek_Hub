import requests


def get_current_exchange():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    data = response.json()
    print(f"Euro\nBuy\t\tSell\n{data[0]['buy']}"
          f"\t{data[0]['sale']}\n")
    print(f"Dollar\nBuy\t\tSell\n{data[1]['buy']}"
          f"\t{data[1]['sale']}\n")


print(get_current_exchange())
