import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# use list to save each article's information
authors = []
titles = []
times = []
push_nums = []
links = []

# craw on ptt
# up to 2023/9/6, the maximum page of CFantasy is 3766
for page in range(1, 3767):
    ptt_url = 'https://www.ptt.cc/bbs/CFantasy/index' + str(page) + '.html'
    resp = requests.get(ptt_url)
    ptt_soup = BeautifulSoup(resp.text, 'html.parser')

    # get all articles
    articles = ptt_soup.find_all('div', class_='r-ent')

    # extract information from each article
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


# connect to MongoDB database and write in
print('all finish')
print('write result in database...')

# password will be hide
mongo_url = "mongodb+srv://lyt0310603:****@cluster0.manfrh4.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_url)
db = client.Learning
collection = db.ptt_CFantasy

new_articles = []
articles_num = len(authors)

for i in range(articles_num):
    new_article = {
        "author": authors[i],
        "title": titles[i],
        "time": times[i],
        "push_num": push_nums[i],
        "url": links[i]
    }
    new_articles.append(new_article)

result = collection.insert_many(new_articles)

client.close()
