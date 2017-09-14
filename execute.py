from nytimesarchive import ArchiveAPI

api = ArchiveAPI('3d07f455158e48a7867a80541a58435b')

def getResults():
    year = input("Please type a year: ")
    month = input("Please type a month: ")
    print(api.query(year, month))

getResults()
