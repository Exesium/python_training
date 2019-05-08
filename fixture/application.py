# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, baseurl):
        # if browser == 'firefox':
        #     self.wd = webdriver.Firefox()
        # elif browser == 'chrome':
        #     self.wd = webdriver.Chrome()
        # elif browser == 'ie':
        #     self.wd = webdriver.Ie()
        # else:
        #     raise ValueError("Unrecognized browser {}".format(browser))
        # *******************************************************************************
        CHROME_PATH = "C:/Program Files (x86)/Google/Chrome Beta/Application/chrome.exe"
        webdriver.ChromeOptions.binary_location = CHROME_PATH
        self.wd = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        self.wd.maximize_window()
        # *******************************************************************************

        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.baseurl = baseurl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not wd.current_url == self.baseurl:
            wd.get(self.baseurl)

    def destroy(self):
        self.wd.quit()
