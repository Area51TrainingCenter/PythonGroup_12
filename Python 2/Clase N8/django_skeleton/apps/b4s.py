from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from selenium import webdriver
import dryscrape

try:
    html = urlopen("https://www.python.org/?q=beautifulsoup")
except HTTPError as e:
    print(e)
except URLError:
    print("El servidor esta fuera de servicio")
else:

    session = dryscrape.Session()
    session.visit("https://www.python.org/?q=beautifulsoup")
    response = session.body()
    res = BeautifulSoup(response)
    print(res.findAll("a",  class_='package-snippet'))
