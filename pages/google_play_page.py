from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class GooglePlayPage(Page):

    def verify_google_play_open(self):
        self.verify_partial_url('https://play.google.com/store/apps/')
