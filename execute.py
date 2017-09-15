from nytimesarchive import ArchiveAPI

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
        if article['section_name']:
            updated_article['section']= article['section_name']
        l.append(updated_article)
        
    return l


x = pullRelevantInfo(getResults())


