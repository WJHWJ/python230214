# web1.py
from bs4 import BeautifulSoup

#파일 읽기
page = open("c:\\work\\test01.html","rt",encoding="utf-8").read()
#검색을 위한 객체
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())