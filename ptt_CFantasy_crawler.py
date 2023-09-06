import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

authors = []
titles = []
times = []
push_nums = []
links = []

for page in range(1, 3767):
    ptt_url = 'https://www.ptt.cc/bbs/CFantasy/index' + str(page) + '.html'
    resp = requests.get(ptt_url)
    ptt_soup = BeautifulSoup(resp.text, 'html.parser')

    articles = ptt_soup.find_all('div', class_='r-ent')

    for article in articles:
        author = article.find('div', class_='author').text
        time = article.find('div', class_='date').text
        title = article.find('div', class_='title').find('a').text
        link = article.find('div', class_='title').find('a')['href']
        push_num = article.find('div', class_='nrec').text

        authors.append(author)
        times.append(time)
        titles.append(title)
        links.append(link)
        push_nums.append(push_num)

    print(page, 'finsh')

print('all finish')
print('write result in database...')

mongo_url = "mongodb+srv://lyt0310603:xjp971403@cluster0.manfrh4.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_url)
db = client.Learning
collection = db.ptt_CFantasy

new_articles = []

for i in range(len(authors)):
    new_article = {
        "author": authors[i],
        "title": titles[i],
        "time": times[i],
        "push_num": push_nums[i],
        "url": links[i]
    }
    new_articles.append(new_article)
print(new_articles)
result = collection.insert_many(new_articles)
client.close()