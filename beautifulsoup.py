import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://feeds.bbci.co.uk/news/rss.xml"

response = requests.get(url, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.content, "xml")

data = []

for news in soup.find_all("item"):

    headline = news.find("title").get_text(strip=True)

    pub_date = news.find("pubDate")

    if pub_date:
        date = pub_date.get_text(strip=True)

        date = datetime.strptime(
            date, "%a, %d %b %Y %H:%M:%S %Z"
        ).strftime("%d-%m-%Y %H:%M")
    else:
        date = "Not available"

    category = news.find("category")

    if category:
        category = category.get_text(strip=True)
    else:
        category = "News"

    data.append([headline, date, category])

with open("news.csv", "w", newline="", encoding="utf-8-sig") as file:

    writer = csv.writer(file)

    writer.writerow(["Headline", "Date", "Category"])

    writer.writerows(data)

print("News headlines saved successfully!")
print("Total headlines:", len(data))