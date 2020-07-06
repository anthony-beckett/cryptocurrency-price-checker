from bs4 import BeautifulSoup
import requests


def to_stop_at(char):
    while price[char].isalpha() is False:
        char += 1
    return char - 2


def to_get_currency(full_data):
    converted_val = ""
    try:
        for i in full_data[1][:40]:
            if i != " ":
                converted_val += i
            else:
                data = str(full_data[1]).replace(converted_val+" ", "")
                return data, converted_val
    except:
        print("Error: Currency not found")
        exit(1)


def to_get_name(data):
    converted_currency = ""
    for j in data:
        if j.isalpha() or j == " ":
            converted_currency += j
        else:
            return converted_currency


def usd_converter(val, convert_to):
    ggl_url = f"https://www.google.com/search?q={val}+usd+to+{convert_to}"
    ggl_page = requests.get(ggl_url)
    soup = BeautifulSoup(ggl_page.content, "html.parser")
    full_data = str(soup.find(id="main")).split("BNeawe iBp4i AP7Wnd\"><div><div class=\"BNeawe iBp4i AP7Wnd\">")
    data, converted_val = to_get_currency(full_data)
    converted_currency = to_get_name(data)
    return converted_val, converted_currency


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
    try:
        us_coin_price = price[106:to_stop_at(106)]
    except:
        print("ERROR: Your coin could not be found")
        exit(1)
    result = currency_chooser(us_coin_price)
    if result != us_coin_price:
        value = result[0]
        currency_name = result[1]
    else:
        value = result
        currency_name = "US dollar"
    print(f"1 {user_coin.title()} is worth {value} {currency_name}")
