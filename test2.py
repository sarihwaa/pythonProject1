from urllib.request import urlopen
import bs4

url ="http://news.naver.com/"
html = urlopen(url)
bs_object = bs4.BeautifulSoup(html.read(), "html.parser")
print(bs_object)