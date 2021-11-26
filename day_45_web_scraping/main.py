from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_ranks = []
article_links = []

articles = soup.find_all(name="tr", class_="athing")
print(articles)
for article in articles:
    article_ranks.append(article.find(name="span", class_="rank").getText())
    article_texts.append(article.find(name="a", class_="titlelink").getText())
    article_links.append(article.find(name="a", class_="titlelink").get("href"))

#
# print(article_ranks)
# print(article_texts)
# print(article_links)















# with open("index.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.prettify())
#
# anchor_text = soup.find_all(name='a')
#
# # print(anchor_text)
#
# for tag in anchor_text:
#     # print(tag)
#     print(tag.get('href'))
#
# heading = soup.find(name="h1", id="name")
#
# print(heading)
#
# new_heading = soup.find(name="h3", class_="heading")
#
# print(new_heading)
