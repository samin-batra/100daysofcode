import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

res = requests.get(URL)
bs = BeautifulSoup(res.text, 'html.parser')
titles = bs.find_all(name="h3",class_="title")

title_text = [title.getText() for title in titles]
print(title_text)
try:
    with open ("must_watch.txt","w") as f:
        for t in title_text:
            f.write(f"{t}\n")
        # f.writelines(title_text)
except:
    print("Something went wrong")