import requests
from bs4 import BeautifulSoup

def money_exchange_rate_by_google(query, to="원"):
    url = f"https://www.google.com/search?q={query}+{to}"
    headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, "lxml")
    div = bs.find("div", attrs={"data-attrid": "Converter"})
    if div is None:
        print("조회 정보가 없습니다.")
        return (0, None, None)
    names = div.find_all("span", attrs={"data-name": True})
    value = div.find("span", attrs={"data-value": True})
    return (value.text, names[0].text, names[1].text)

def money_exchange_rate_by_naver(query, to="원"):
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}+{to}&ackey=equcykel"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, "lxml")
    currenies = bs.select("span.nt_eng._code")
    value = bs.select_one("strong.price")
    if value is None:
        print("조회 정보가 없습니다.")
        return (0, None, None)
    return (value.text, currenies[0].text, currenies[1].text)

if __name__ == "__main__":
    print(money_exchange_rate_by_google("100달러"))
    print(money_exchange_rate_by_naver("100달러"))