from bs4 import BeautifulSoup

with open ("file.html", "r") as f:
    html = f.read()


soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())

# print(soup.title.text)
# print(soup.p["class"])
# print(soup.find_all("a"))
# print(soup.find(id = "link3"))

# to get all likns

for i in soup.find_all("a"):
    print(i.get("href"))