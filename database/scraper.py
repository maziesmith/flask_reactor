import os
import requests
from bs4 import BeautifulSoup
from .database import SessionLocal, engine
from database import models
from .models import News
from secrets import SCRAPER_TARGET

# db open
db = SessionLocal()
models.Base.metadata.create_all(bind=engine)

# SCRAPE_TARGET = os.environ.get('scraper_target')

# scrape
res = requests.get(SCRAPER_TARGET, headers={'User-Agent': 'MOzilla/5.0'})
chemical_soup = BeautifulSoup(res.text, 'html.parser')
soup_list = chemical_soup.find_all('h2')



# clean 
db_list = []
for news in soup_list:
    tag = news.select('a')
    if tag != []:
        link = news.select('a')[0].get('href')
        text = news.select('a')[0].getText()
        db_list.append((link, text))
    

# add to db
if (len(db_list) > 0):
    retrieve = db.query(News).delete()
    for item in db_list:
        data = models.News(
            link = item[0],
            text = item[1]
        )
        db.add(data)
        db.commit()
    print('added to db')
    db.close()
else:
    print('no data was scraped')
