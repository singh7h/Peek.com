from Utilites.Config import *
from Pages.Search_Page import SearchPage
from selenium.webdriver.common.by import By
import pytest
import time


class TestPersonalityQuiz:

    @pytest.fixture()
    def setup(self):
        self.driver = driver_path("chrome")
        self.sp = SearchPage(self.driver)

    def test_display_all_category_on_experience_search(self, setup):
        """
        Verify all the category are display on experience  search for destination
        :param setup:
        :return:
        """
        self.sp.open_url("https://www.peek.com")
        time.sleep(2)
        self.sp.search_by_destination("San Francisco")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("San Francisco")
        self.sp.search_by_experience("Boat")
        wait_for_page_load()
        self.sp.click_search_experience_button()
        wait_for_page_load()
        self.sp.display_all_category()

    def test_select_category_on_experience_search(self, setup):
        """
        verify user can search category for experience user has searched
        :param setup:
        :return:
        """
        self.sp.open_url("https://www.peek.com")
        time.sleep(2)
        self.sp.search_by_destination("San Francisco")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("San Francisco")
        self.sp.search_by_experience("Boat")
        wait_for_page_load()
        self.sp.click_search_experience_button()
        wait_for_page_load()
        self.sp.display_all_category()
        wait_for_page_load()
        self.sp.select_category("Water Sports")

    def test_select_category_and_display_category_result(self, setup):
        """
        verify user can select the category and display results for particular category
        :param setup:
        :return:
        """
        self.sp.open_url("https://www.peek.com")
        time.sleep(2)
        self.sp.search_by_destination("San Francisco")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("San Francisco")
        self.sp.search_by_experience("Boat")
        wait_for_page_load()
        self.sp.click_search_experience_button()
        wait_for_page_load()
        self.sp.display_all_category()
        wait_for_page_load()
        self.sp.select_category("Water Sports")
        wait_for_page_load()
        self.sp.display_result_for_selected_category()

    def test_select_category_and_category_option(self, setup):
        """
        verify the user can select category and category option
        :param setup:
        :return:
        """
        self.sp.open_url("https://www.peek.com")
        time.sleep(2)
        self.sp.search_by_destination("San Francisco")
        wait_for_page_load()
        self.sp.click_search_destination_button()
        wait_for_page_load()
        self.sp.valid_region_in_banner("San Francisco")
        self.sp.search_by_experience("Boat")
        wait_for_page_load()
        self.sp.click_search_experience_button()
        wait_for_page_load()
        self.sp.display_all_category()
        wait_for_page_load()
        self.sp.select_category("Water Sports")
        wait_for_page_load()
        self.sp.display_result_for_selected_category()
        wait_for_page_load()
        self.sp.select_option_from_category_result("Stand Up Paddle Board Rental in San Rafael")
        wait_for_page_load()

    def teardown(self):
        self.driver.close()
        self.driver.quit()

