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
        assert 'YouTube' in driver.title
        elem = driver.find_element_by_id("masthead-search-term")
        elem.send_keys("TheBroadwayShow")
        elem.send_keys("TheBroad")
        elem.send_keys("way")
        elem.send_keys('S')
        elem.send_keys('how')
        elem1 = driver.find_element_by_id("search-btn")
        elem1.click()
        elem2 = driver.find_element_by_class_name("yt-lockup-title")
        assert elem2.is_displayed()
        elem2.click()
        elem3 = driver.find_element_by_class_name("subscribe-label")
        assert elem3.is_displayed()
        elem3.click()
        driver.close()


if __name__ == '__main__':
    unittest.main()
