from bs4 import BeautifulSoup
import requests


def to_stop_at(char):
    while price[char].isalpha() is False:
        char += 1
    return char-2


def USD_to_Other(val, convert_to):
    ggl_url = f"google.com/search?q={val}+us+dollar+to+{convert_to}"
    ggl_page = requests.get(ggl_url)
    soup = BeautifulSoup(ggl_page.content, "html.parser")
    results = soup.find("div", id="knowledge-currency__updatable-data-column")
    results.find_all("div", class_="dDoNo vk_bk gsrt gzfeS")
    return results

def currency_chooser(US_val, coin):
    currency = input("Enter currency you wish to see: ")
    if currency == "USD":
        return US_val
    else:
        return USD_to_Other(US_val, currency.replace(" ", "+"))


def get_crypto(coin):
    url = f"https://coinmarketcap.com/currencies/{coin}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return str(soup.find_all("div", class_="cmc-details-panel-price jta9t4-0 fcilTk"))
    

if __name__ == "__main__":
    user_coin = input("Enter a cryptocoin to find its price: ").lower()
    price = get_crypto(user_coin)
    US_coin_price = price[106:to_stop_at(105)].replace(",", "")
    print(currency_chooser(US_coin_price, user_coin))
