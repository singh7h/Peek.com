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
        """
        Verify the url for peek.com
        :param setup:
        :return:
        """
        print("The test case start: test_valid_the_url")
        self.sp.open_url("https://www.peek.com")
        self.driver.maximize_window()
        url = self.driver.current_url
        if "peek.com" in url:
            print("Test_case is Pass")
        else:
            print("Test_case is Failed")
        print("The test case ended: test_valid_the_url")

    def test_verify_search_option_displaying(self, setup):
        """
        Verify search option is displaying
        :param setup:
        :return:
        """
        print("The test case start: test_verify_search_option_displaying")
        self.sp.open_url("https://www.peek.com")
        self.sp.valid_search_option_displaying()
        print("The test case ended: test_verify_search_option_displaying")

    def test_verify_search_destination_is_displaying_in_url_and_banner(self, setup):
        """
        verify destination searched is displayin in url and banner
        :param setup:
        :return:
        """
        print("The test case start: test_verify_search_destination_is_displaying_in_url_and_banner")
        self.sp.open_url("https://www.peek.com")
        time.sleep(2)
        self.sp.search_by_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        wait_for_page_load()
        url = self.driver.current_url
        if "Minneapolis" in url:
            print("Test_case is Pass")
        else:
            print("Test_case is Failed")
        print("The test case ended: test_verify_search_destination_is_displaying_in_url_and_banner")

    def test_verify_search_experience_without_filters(self, setup):
        """
        verify the search experience display without using the any filters
        :param setup:
        :return:
        """
        print("The test case start: test_verify_search_experience_without_filters")
        self.sp.open_url("https://www.peek.com")
        wait_for_page_load()
        self.sp.search_by_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        self.sp.display_all_search_result()
        print("The test case ended: test_verify_search_experience_without_filters")

    def test_verify_search_experience_with_sort_by_most_popular(self, setup):
        """
        verify the search experience are display by most popular option
        :param setup:
        :return:
        """
        print("The test case start: test_verify_search_experience_without_filters")
        self.sp.open_url("https://www.peek.com")
        wait_for_page_load()
        self.sp.search_by_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        self.sp.use_filter_sort_by("mostpopular")
        wait_for_page_load()
        self.sp.display_all_search_result()
        print("The test case ended: test_verify_search_experience_without_filters")

    def test_verify_search_experience_with_sort_by_lowest_price(self, setup):
        """
        verify the search experience are display by most popular option
        :param setup:
        :return:
        """
        print("The test case start: test_verify_search_experience_with_sort_by_lowest_price")
        self.sp.open_url("https://www.peek.com")
        wait_for_page_load()
        self.sp.search_by_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        self.sp.use_filter_sort_by("lowestprice")
        wait_for_page_load()
        self.sp.display_all_search_result()
        print("The test case ended: test_verify_search_experience_with_sort_by_lowest_price")

    def test_verify_search_experience_with_under50_price_filters(self, setup):
        """
        verify experience search display for under 50 price filter
        :param setup:
        :return:
        """
        print("The test case start: test_verify_search_experience_with_under50_price_filters")
        self.sp.open_url("https://www.peek.com")
        self.sp.open_url("https://www.peek.com")
        wait_for_page_load()
        self.sp.search_by_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        wait_for_page_load()
        self.sp.use_filter_price_by("under50")
        wait_for_page_load()
        self.sp.display_all_search_result()
        print("The test case ended: test_verify_search_experience_with_under50_price_filters")

    def test_verify_search_experience_with_50_to_100_price_filters(self, setup):
        """
         verify experience search display for under 50 to 100 price filter
        :param setup:
        :return:
        """
        print("The test case start: test_verify_search_experience_with_50_to_100_price_filters")
        self.sp.open_url("https://www.peek.com")
        wait_for_page_load()
        self.sp.search_by_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        wait_for_page_load()
        self.sp.use_filter_price_by("50-100")
        wait_for_page_load()
        self.sp.display_all_search_result()
        print("The test case ended: test_verify_search_experience_with_50_to_100_price_filters")

    def test_verify_search_experience_with_100_to_150__price_filters(self, setup):
        """
         verify experience search display for under 100 to 150 price filter
        :param setup:
        :return:
        """
        print("The test case start: test_verify_search_experience_with_100_to_150__price_filters")
        self.sp.open_url("https://www.peek.com")
        wait_for_page_load()
        self.sp.search_by_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        wait_for_page_load()
        self.sp.use_filter_price_by("100-150")
        wait_for_page_load()
        self.sp.display_all_search_result()
        print("The test case ended: test_verify_search_experience_with_100_to_150__price_filters")

    def test_verify_search_experience_with_over250_price_filters(self, setup):
        """
        verify experience search display for under over250 price filter
        :param setup:
        :return:
        """
        print("The test case start: test_verify_search_experience_with_over250_price_filters")
        self.sp.open_url("https://www.peek.com")
        wait_for_page_load()
        self.sp.search_by_destination("Minneapolis")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("Minneapolis")
        wait_for_page_load()
        self.sp.use_filter_price_by("over250")
        wait_for_page_load()
        self.sp.display_all_search_result()
        print("The test case ended: test_verify_search_experience_with_over250_price_filters")

    def teardown(self):
        self.driver.close()
        self.driver.quit()
