from bs4 import BeautifulSoup
import requests
# with open("website.html",encoding="utf8") as f:
#     t = f.read()
#     # print(t)
#
# soup = BeautifulSoup(t, 'html.parser' )

response = requests.get("https://news.ycombinator.com/")
# print(response.text)

h_news = BeautifulSoup(response.text, 'html.parser')
anchor = h_news.select("a.titlelink")
article_texts = []
article_links = []
for a in anchor:
    article_texts.append(a.getText())
    article_links.append(a.get("href"))

# print(anchor.getText())
#
# article_link = anchor.attrs['href']

upvotes = [int(upvote.getText().split(" ")[0])for upvote in h_news.find_all(name="span",class_="score")]
# print(upvotes.getText())
# article_score = upvotes.getText()
index, max_elem = 0,-2
for ind in range(0, len(upvotes)):
    if upvotes[ind]>max_elem:
        max_elem = upvotes[ind]
        index = ind

print(f"Article with most upvotes is {article_texts[index]}. Link: {article_links[index]}. Upvotes: {upvotes[index]}")
# print(article_links)
# print(article_texts)
# print(upvotes)

# first_link = anchor
# print(first_link)
# print(h_news.prettify())