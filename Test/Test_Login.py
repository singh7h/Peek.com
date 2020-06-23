from pages.base_page import *
from pages.Drivers import *
import pytest
import time


class TestLogin:

    @pytest.fixture()
    def setup(self):
        self.driver = drivers("chrome")
        self.bp = BasePage(self.driver)

    @pytest.mark.parametrize('tcid',["1","2","3"])
    def test_open_url(self, setup, tcid):
        self.bp.open_browser("https://www.tesla.com")
        time.sleep(2)
        # self.driver.find_element(object_properties.visit_button).click()
        # self.driver.find_element_by_class_name("tds-o-btn_group--item").click()
        time.sleep(2)

    def teardown(self):
        self.driver.close()
        self.driver.quit()
