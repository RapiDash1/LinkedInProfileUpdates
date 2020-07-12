from bs4 import BeautifulSoup
from PageInfo import PageInfo

class ParseInfo():

    def postViews(self, pageInfo):
        soup = BeautifulSoup(pageInfo)
        linkedInInfo = soup.find_all("span", class_="feed-identity-module__stat link-without-visited-state")
        views = linkedInInfo[-1].getText()
        return views

