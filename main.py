from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates, CurrencyCodes
import requests


def to_stop_at(char):
    while price[char].isalpha() is False:
        char += 1
    return char-2


def main():
    while True:
        currency = input("Enter currency you wish to see: ").upper()
        if currency == "USD":
            coin_price = US_coin_price
        else:
            try:
                coin_price = CurrencyRates().convert('USD', currency, US_coin_price)
            except:
                print("\nCurrency not found, using USD.\n")
                print("The list of currency codes may be found here: https://bit.ly/CurrencyCodes\n")
                currency = "USD"
                coin_price = US_coin_price
                break
    return f"{coin.title()} is worth {CurrencyCodes().get_symbol(currency)}{coin_price}"


if __name__ == "__main__":
    coin = input("Enter a cryptocoin to find its price: ").lower()
    url = f"https://coinmarketcap.com/currencies/{coin}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='ResultsContainer')
    price = str(soup.find_all("div", class_="cmc-details-panel-price jta9t4-0 fcilTk"))

    US_coin_price = price[106:to_stop_at(105)].replace(",", "")
    print(main())