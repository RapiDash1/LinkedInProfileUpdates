from PageInfo import PageInfo
from ParseInfo import ParseInfo
from mail import Email

class PostViewsUpdate():

    def __init__(self):
        self._pageInfo = PageInfo()

    def pageInfo(self): return self._pageInfo


    def sendEmail(self, updatedPostViews):
        email = Email()
        email.send(updatedPostViews)


    def updateViews(self):
        postViews = ParseInfo().postViews(self.pageInfo().makeRequest())
        self.sendEmail(postViews)


if __name__ == "__main__":
    updatedViews = PostViewsUpdate()
    updatedViews.updateViews()
