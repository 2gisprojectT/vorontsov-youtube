# -*- coding: utf-8 -*-
__author__ = 'Владислав'


from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class YoutubeTest(TestCase):

    def test_search(self):
        driver = webdriver.Firefox()
        driver.get("http://youtube.com/")
        elem = driver.find_element_by_id("masthead-search-term")
        elem.send_keys("TheBroadwayShow")
        elem1 = driver.find_element_by_id("search-btn")
        elem1.click()
        elem2 = driver.find_element_by_class_name("yt-lockup-title")
        elem2.click()
        elem3 = driver.find_element_by_class_name("subscribe-label")
        elem3.click()
        driver.close()

if __name__ == '__main__':
    unittest.main()
