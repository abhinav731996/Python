import bs4
import requests

url = "https://www.codewithharry.com/blog"

data = requests.get(url)

soup = bs4.BeautifulSoup(data.text,"html.parser")

# print(soup.prettify())

# for para in soup.find_all("p"):
#     print(para.text) 

for link in soup.find_all("a"):
    lnk = link.get("href")
    if lnk and lnk.startswith("http"):
        print(lnk)