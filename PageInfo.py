from selenium import webdriver
import linkedInInfo
import os

class PageInfo():

    def __init__(self, path=""):
        self._path = path if path != "" else "feed"


    def path(self): return self._path
    def setPath(self, path):
        self._path = path
    

    def makeRequest(self):
        driver = webdriver.Chrome(os.getcwd()+"/chromedriver")

        url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
        driver.get(url)

        username = driver.find_element_by_id("username")
        password = driver.find_element_by_id("password")

        """
            Save password and username in linkedInInfo.py as follows:
                userNameStr = your_username
                passwordStr = yout_password
        """
        username.send_keys(linkedInInfo.userNameStr)
        password.send_keys(linkedInInfo.passwordStr)
        form = driver.find_element_by_tag_name("form")
        form.submit()

        return driver.page_source