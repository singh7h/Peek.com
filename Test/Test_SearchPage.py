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

    def test_valid_the_url(self, setup):
        self.sp.open_url("https://www.peek.com")
        self.driver.maximize_window()
        url = self.driver.current_url
        if "peek.com" in url:
            print("Test_case is Pass")
        else:
            print("Test_case is Failed")

    def test_verify_search_option_displaying(self, setup):
        self.sp.open_url("https://www.peek.com")
        self.sp.valid_search_option_displaying()

    def test_verify_search_destination(self, setup):
        self.sp.open_url("https://www.peek.com")
        time.sleep(2)
        self.sp.search_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        wait_for_page_load()
        url = self.driver.current_url
        if "Minneapolis" in url:
            print("Test_case is Pass")
        else:
            print("Test_case is Failed")

    def test_verify_search_destination_without_filters(self, setup):
        self.sp.open_url("https://www.peek.com")
        wait_for_page_load()
        self.sp.search_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        self.sp.print_search_result()

    def test_verify_search_destination_with_most_popular_filters(self, setup):
        self.sp.open_url("https://www.peek.com")
        wait_for_page_load()
        self.sp.search_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        self.sp.result_sort_by("mostpopular")
        wait_for_page_load()
        self.sp.print_search_result()

    def test_verify_search_destination_with_lowest_price_filters(self, setup):
        self.sp.open_url("https://www.peek.com")
        wait_for_page_load()
        self.sp.search_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        self.sp.result_sort_by("lowestprice")
        wait_for_page_load()
        self.sp.print_search_result()

    def teardown(self):
        self.driver.close()
        self.driver.quit()
