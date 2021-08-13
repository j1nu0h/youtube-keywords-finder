

from bs4 import BeautifulSoup
import requests

def get_keywords(code):
    URL = "http://youtube.com/watch?v="
    URL += code

    response = requests.get(URL)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    keywords = soup.find("meta", attrs={"name": "keywords"})
    return keywords["content"]
