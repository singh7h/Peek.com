from Utilities.Config import *
from Pages.Search_Page import SearchPage
import pytest


class TestBooking:

    @pytest.fixture()
    def setup(self):
        self.driver = driver_path("chrome")
        self.sp = SearchPage(self.driver)

    def test_activity_calendar_widget_populates_with_bookable_days(self, setup):
        """
        verify activity calendar shows th calender widget with bookable days for current month
        :param setup:
        :return:
        """
        self.sp.open_url("https://www.peek.com")
        self.sp.search_by_destination("San Francisco")
        self.sp.click_search_destination_button()
        self.sp.valid_region_in_banner("San Francisco")
        self.sp.search_by_experience("Boat")
        self.sp.click_search_experience_button()
        self.sp.display_all_category()
        self.sp.select_category("Water Sports")
        self.sp.display_result_for_selected_category()
        self.sp.select_option_from_category_result("Stand Up Paddle Board Rental in San Rafael")
        wait_for_page_load()
        self.sp.available_days_for_booking()

    def test_book_now_button_open_widget_timeslot_and_ticket(self, setup):
        """
        verify activity user can select bookable days and time for from widget
        :param setup:
        :return:
        """
        self.sp.open_url("https://www.peek.com")
        self.sp.search_by_destination("San Francisco")
        self.sp.click_search_destination_button()
        self.sp.valid_region_in_banner("San Francisco")
        self.sp.search_by_experience("Boat")
        self.sp.click_search_experience_button()
        self.sp.display_all_category()
        self.sp.select_category("Water Sports")
        self.sp.display_result_for_selected_category()
        self.sp.select_option_from_category_result("Stand Up Paddle Board Rental in San Rafael")
        wait_for_page_load()
        self.sp.click_book_now_button()
        wait_for_page_load()
        wait_for_page_load()
        self.driver.switch_to_frame(1)
        self.sp.select_date_from_widget("27")
        self.sp.select_time_available_from_widget("11:00am")

    def test_incresing_number_ticket_prevent_booking(self, setup):
        """
        verify increasing the number of selected tickets beyond the
        availability prevents me from booking that timeslot
        :param setup:
        :return:
        """
        self.sp.open_url("https://www.peek.com")
        self.sp.search_by_destination("San Francisco")
        self.sp.click_search_destination_button()
        self.sp.valid_region_in_banner("San Francisco")
        self.sp.search_by_experience("Boat")
        self.sp.click_search_experience_button()
        self.sp.display_all_category()
        self.sp.select_category("Water Sports")
        self.sp.display_result_for_selected_category()
        self.sp.select_option_from_category_result("Stand Up Paddle Board Rental in San Rafael")
        wait_for_page_load()
        self.sp.click_book_now_button()
        wait_for_page_load()
        wait_for_page_load()
        self.driver.switch_to_frame(1)
        wait_for_page_load()
        self.sp.select_date_from_widget("27")
        self.sp.select_time_available_from_widget("11:00am")
        self.sp.select_number_ticket()

    def teardown(self):
        self.driver.close()
        self.driver.quit()
