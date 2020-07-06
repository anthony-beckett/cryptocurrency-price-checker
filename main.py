from bs4 import BeautifulSoup
import requests


def to_stop_at(char):
    while price[char].isalpha() is False:
        char += 1
    return char-2


def usd_converter(val, convert_to):
    ggl_url = f"https://www.google.com/search?q={val}+usd+to+{convert_to}"
    ggl_page = requests.get(ggl_url)
    soup = BeautifulSoup(ggl_page.content, "html.parser")
    return str(soup.find_all("div", class_="dDoNo vk_bk gsrt gzfeS"))


def currency_chooser(us_val):
    currency = input("Enter currency you wish to see: ").replace(" ", "+")
    return usd_converter(us_val, currency) if currency != "USD" else us_val


def get_crypto(coin):
    url = f"https://coinmarketcap.com/currencies/{coin}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return str(soup.find_all("div", class_="cmc-details-panel-price jta9t4-0 fcilTk"))
    

if __name__ == "__main__":
    user_coin = input("Enter a cryptocoin to find its price: ").lower()
    price = get_crypto(user_coin)
    us_coin_price = price[106:to_stop_at(106)]
    print(us_coin_price)
    result = currency_chooser(us_coin_price)
    currency_name = "currency_placeholder"
    print(f"{user_coin.title()} is worth {result} {currency_name}")
