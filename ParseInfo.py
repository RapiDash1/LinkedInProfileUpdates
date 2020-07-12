from bs4 import BeautifulSoup
from PageInfo import PageInfo

class ParseInfo():

    def __init__(self, pageInfo):
        self._pageInfo = pageInfo
    
    def pageInfo(self): return self._pageInfo


    def postViews(self):
        soup = BeautifulSoup(self.pageInfo())
        linkedInInfo = soup.find_all("span", class_="feed-identity-module__stat link-without-visited-state")
        views = linkedInInfo[-1].getText()
        return views

