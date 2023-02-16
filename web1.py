# web1.py
from bs4 import BeautifulSoup

#파일 읽기
page = open("c:\\work\\test01.html","rt",encoding="utf-8").read()
#검색을 위한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#<p>전부 검색: list형태로 리턴
#print(soup.find_all("p"))
#<a>전부 검색
#print(soup.find_all("a"))
#<p class="outer-text">이런 조건
#print(soup.find_all("p", class_="outer-text"))

#태그 내부의 문자열: .text 속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    #title = title.replace("\n", "")
    print(title)