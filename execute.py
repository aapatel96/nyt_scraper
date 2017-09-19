from nytimesarchive import ArchiveAPI
import os
import pymongo

client = pymongo.MongoClient('mongodb://heroku_d0df7lpt:i4k9nglftvest2g14p69tkrbph@ds135534.mlab.com:35534/heroku_d0df7lpt')
db = client.get_default_database()

articles = db['articles']

api = ArchiveAPI('3d07f455158e48a7867a80541a58435b')

def getResults():
    year = int(input("Please type a year: "))
    month = int(input("Please type a month: "))
    x = api.query(year, month)
    return x['response']['docs']

def pullRelevantInfo(docs):
    l = []
    for article in docs:
        updated_article={'web_url':article['web_url'],
                  'pub_date':article['pub_date'],
                  'headline':article['headline'],
                  'snippet':article['snippet']
                  }
        try:
            updated_article['section']= article['section_name']
        except:
            pass
        articles.insert_one(updated_article)
        l.append(updated_article)
    return l


x = pullRelevantInfo(getResults())
