from bs4 import BeautifulSoup
import requests

num = 1
article_texts = []
article_price = []
article_links = []

WEBSITE = "https://www.olx.pt"
page = 1

search_query = (input("Please write what you want to search: ")).replace(" ","-")

response = requests.get(f"https://www.olx.pt/ads/q-{search_query}/?page={page}")
website = response.text

soup = BeautifulSoup(website,"lxml")
pages_label = soup.find(name="div", class_="css-4mw0p4")
total_pages = pages_label.find_all("a")
pages = int(total_pages[-2].getText())
total_count = soup.find(name="a", class_="css-b6tdh7")
print("------------------------------")
print("\n"+total_count.text+"\n")
print("------------------------------")
print(f"\nTotal Pages: {pages}\n")
print("------------------------------")

while page <= pages:
    response = requests.get(f"https://www.olx.pt/ads/q-{search_query}/?page={page}")
    website = response.text

    soup = BeautifulSoup(website,"lxml")
    articles = soup.find_all(name="div", class_="css-1apmciz")

    for article_tag in articles:
        #get title
        text_tag = article_tag.find("h4")
        text = text_tag.getText()
        article_texts.append(text)
            #get price
        price_tag = article_tag.find("p")
        price = price_tag.getText().split()[0]
        article_price.append(price)
            #get link
        link_tag = article_tag.find("a")
        link = link_tag.get("href")
        if link[0]=="/":
            article_links.append(WEBSITE+link)
        else:
            article_links.append(link)
    page+=1
    
for name, price, link in zip(article_texts, article_price, article_links):
        print(f"{num}. {name} - {price}€ - {link}")
        num+=1
