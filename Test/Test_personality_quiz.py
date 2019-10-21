from Utilites.Config import *
from Pages.Search_Page import SearchPage
from selenium.webdriver.common.by import By
import pytest
import time


class TestHomePage:

    @pytest.fixture()
    def setup(self):
        self.driver = driver_path("chrome")
        self.sp = SearchPage(self.driver)

    def test_verify_search_destination(self, setup):
        self.sp.open_url("https://www.peek.com")
        time.sleep(2)
        self.sp.search_destination("San Francisco")
        wait_for_page_load()
        self.sp.click_search_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("San Francisco")
        wait_for_page_load()
        url = self.driver.current_url
        if "Francisco" in url:
            print("Test_case is Pass")
        else:
            print("Test_case is Failed")

    def test_display_all_classification_for_destination(self, setup):
        """
        display all classification for destination
        :param setup:
        :return:
        """
        self.sp.open_url("https://www.peek.com")
        time.sleep(2)
        self.sp.search_destination("San Francisco")
        wait_for_page_load()
        self.sp.click_search_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("San Francisco")
        self.sp.display_all_classification()

    def test_display_classification_on_experience_search(self, setup):
        self.sp.open_url("https://www.peek.com")
        time.sleep(2)
        self.sp.search_destination("San Francisco")
        wait_for_page_load()
        self.sp.click_search_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("San Francisco")
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[6]").send_keys("pizza")
        self.driver.find_element_by_xpath("(//BUTTON[@type='submit'][text()='SEARCH'][text()='SEARCH'])[2]").click()
        wait_for_page_load()
        self.sp.display_all_classification()

    def test_display_search_on_experience_search(self, setup):
        self.sp.open_url("https://www.peek.com")
        time.sleep(2)
        self.sp.search_destination("San Francisco")
        wait_for_page_load()
        self.sp.click_search_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("San Francisco")
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[6]").send_keys("Boat")
        wait_for_page_load()
        self.driver.find_element_by_xpath("(//BUTTON[@type='submit'][text()='SEARCH'][text()='SEARCH'])[2]").click()
        wait_for_page_load()
        self.sp.display_all_classification()
        wait_for_page_load()
        print(self.driver.find_element_by_class_name("containers-Search-styles---activities").text)
        self.driver.find_element_by_xpath("")






    def teardown(self):
        self.driver.close()
        self.driver.quit()

