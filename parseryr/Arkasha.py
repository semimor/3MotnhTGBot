from pprint import pprint
import requests
from bs4 import BeautifulSoup as BS


URL = "https://megogo.net/ru/films"

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

def get_html(url , params=''):
    req = requests.get(url=url, headers=HEADERS , params= params)
    return req

def get_data(html):
    soup = BS(html ,"html.parser")
    items = soup.find_all("div" , class_="card-content video-content")
    anime =[]
    for item in items:
        links = item.find("a").get("href")
        anime.append({
            "link" : links,
            "title" : item.find("h3","video-title card-content-title").getText().strip(),
            "year" : item.find("span" , "video-year").getText(),
            "gengre": item.find("span" , "video-country").getText()
        })
    # anime.append(photo)
    return anime
#
def parser():
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Next", callback_data="button_call_1")
    markup.add(button_call_1)
    html = get_html(URL)
    if html.status_code == 200:
        ans = get_data(html.text)
        return ans
    else:
        raise Exception("Ошибка!")