from nytimesarchive import ArchiveAPI
import pymongo

client = pymongo.MongoClient('mongodb://heroku_d0df7lpt:i4k9nglftvest2g14p69tkrbph@ds135534.mlab.com:35534/heroku_d0df7lpt')
db = client.get_default_database()

articles = db['articles']

api = ArchiveAPI('3d07f455158e48a7867a80541a58435b')

def getResults(year, month):
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
        if article['section_name']:
            updated_article['section']= article['section_name']
        ##articles.insert_one(updated_article) this is commented out because I do not want to risk double adding the articles in the db
        l.append(updated_article)

    return l

newslists ={}
for year in range(1997,2018):
  articles = pullRelevantInfo(getResults(year,11))
  newslists[year]=articles
