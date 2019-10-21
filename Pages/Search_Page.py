from Pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
import time


class SearchPage(BasePage):

    # Locator for the Search Page
    destination = "(//INPUT[@type='text'])[1]"
    from_date = "(//INPUT[@type='text'])[7]"
    to_date = "(//INPUT[@type='text'])[8]"
    search_button = "(//BUTTON[@type='submit'][text()='SEARCH'][text()='SEARCH'])[1]"
    banner_region_title = "(//STRONG)[1]"
    search_result = "//*[@id='content']/div/div[1]/div/div[2]/div/div[2]/div[3]"
    sort_by = ".sticky-inner-wrapper .padding-xs .containers-Search-styles---selectedSortByOrPriceFilters"

    def valid_search_option_displaying(self):
        try:
            if self.driver.find_element_by_xpath(self.destination).is_displayed():
                print("Search option is Displaying")
            else:
                print("Search options not displaying")
        except Exception as e:
            print(str(e))

    def valid_from_date(self, date):
        try:
            if self.driver.find_element_by_xpath(self.from_date):
                self.driver.find_element_by_xpath(self.from_date).clear()
                self.driver.find_element_by_xpath(self.from_date).send_keys(date)
                print(date + " From Date is entered ")
            else:
                print("From date options is not displaying")
        except Exception as e:
            print(str(e))

    def valid_to_date(self, date):
        try:
            if self.driver.find_element_by_xpath(self.to_date).is_displayed():
                self.driver.find_element_by_xpath(self.to_date).send_keys(Keys.CLEAR)

                print(date + " To Date is entered ")
            else:
                print("TO date options is not displaying")
        except Exception as e:
            print(str(e))

    def click_search_button(self):
        try:
            self.driver.find_element_by_xpath(self.search_button).click()
        except Exception as e:
            print(str(e))

    def valid_region_in_banner(self, destination):
        try:
            if self.driver.find_element_by_xpath(self.banner_region_title):
                banner_value = self.driver.find_element_by_xpath(self.banner_region_title).text
                if str(banner_value).lower() == destination.lower():
                    print(banner_value + "Name is same as " + destination)
                else:
                    print(banner_value + "Name is same as " + destination)
            else:
                print("TO date options is not displaying")
        except Exception as e:
            print(str(e))

    def search_destination(self, destination):
        try:
            if self.driver.find_element_by_xpath(self.destination):
                self.driver.find_element_by_xpath(self.destination).send_keys(destination)
                time.sleep(2)
                self.driver.find_element_by_xpath(self.destination).send_keys(Keys.ENTER)
                print(destination + " is entered as destination")
            else:
                print("search options not displaying")
        except Exception as e:
            print(str(e))

    def print_search_result(self):
        try:
            if self.driver.find_element_by_xpath(self.search_result):
                table = self.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/div[2]/div/div[2]/div[3]")
                table_row = table.find_elements_by_tag_name("h4")
                for row in table_row:
                    print("The activity in destination: " + row.text)
            else:
                print("search result is not displaying")
        except Exception as e:
            print(str(e))

    def result_sort_by(self,sort_option):
        try:
            if self.driver.find_element_by_css_selector(self.sort_by):
                self.driver.find_element_by_css_selector(self.sort_by).click()
                time.sleep(2)
                if sort_option.lower() == "lowestprice":
                    self.driver.find_element_by_link_text("Lowest Price").click()
                elif sort_option.lower() == "mostpopular":
                    self.driver.find_element_by_link_text("Most Popular").click()
                else:
                    print("sort by is not correct")
            print("sort by option is not displaying")
        except Exception as e:
            print(str(e))

    def display_all_classification(self):
        try:
            if self.driver.find_element_by_class_name("margin-xs-right").is_displayed():
                current_value=self.driver.find_element_by_class_name("margin-xs-right").text
                print(current_value)
            else:
                print("the classification option not displaying")
        except Exception as e:
            print(str(e))





