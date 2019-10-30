from Pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Utilites.Config import *


class SearchPage(BasePage):

    # Locator for the Search Page
    input_destination = "(//INPUT[@type='text'])[1]"
    from_date = "(//INPUT[@type='text'])[7]"
    to_date = "(//INPUT[@type='text'])[8]"
    search_for_destination_button = "(//BUTTON[@type='submit'][text()='SEARCH'][text()='SEARCH'])[1]"
    banner_region_title = "(//STRONG)[1]"
    search_result = "//*[@id='content']/div/div[1]/div/div[2]/div/div[2]/div[3]"
    sort_by = ".sticky-inner-wrapper .padding-xs .containers-Search-styles---selectedSortByOrPriceFilters"
    filter_by_price = ".sticky-inner-wrapper .containers-Search-styles---pricesContainer .containers-Search-" \
                      "styles---selectedSortByOrPriceFilters"
    checkbox_under_50 = "(//input[@name='Under $50'])[2]"
    checkbox_50_100 = "(//input[@name='$50 - $100'])[2]"
    checkbox_100_250 = "(//input[@name='$100 - $150'])[2]"
    checkbox_over_250 = "(//input[@name='Over $250'])[2]"
    input_experience = "(//INPUT[@type='text'])[6]"
    search_for_experience_button = "(//BUTTON[@type='submit'][text()='SEARCH'][text()='SEARCH'])[2]"
    category_option = "//H4[@class='components-ActivityRow-style---title padding-sm-top padding-sm-bottom margin-none']"

    def valid_search_option_displaying(self):
        try:
            if self.driver.find_element_by_xpath(self.input_destination).is_displayed():
                print("Search option is Displaying and this step is failed")
            else:
                print("Search options not displaying and this step is failed")
        except Exception as e:
            print(str(e))

    def valid_from_date(self, date):
        try:
            if self.driver.find_element_by_xpath(self.from_date):
                self.driver.find_element_by_xpath(self.from_date).clear()
                self.driver.find_element_by_xpath(self.from_date).send_keys(date)
                print(date + " From Date is entered  and this step is passed")
            else:
                print("From date options is not displaying and this step is failed")
        except Exception as e:
            print(str(e))

    def valid_to_date(self, date):
        try:
            if self.driver.find_element_by_xpath(self.to_date).is_displayed():
                self.driver.find_element_by_xpath(self.to_date).send_keys(Keys.CLEAR)

                print(date + " To Date is entered and this step is passed ")
            else:
                print("TO date options is not displaying and this step is failed")
        except Exception as e:
            print(str(e))

    def click_search_destination_button(self):
        try:
            self.driver.find_element_by_xpath(self.search_for_destination_button).click()
            print("The destination search button is clicked and this step is passed")
        except Exception as e:
            print(str(e))

    def click_search_experience_button(self):
        try:
            self.driver.find_element_by_xpath(self.search_for_experience_button).click()
            print("The experience search button is clicked and this step is passed")
        except Exception as e:
            print(str(e))

    def valid_region_in_banner(self, destination):
        try:
            if self.driver.find_element_by_xpath(self.banner_region_title):
                banner_value = self.driver.find_element_by_xpath(self.banner_region_title).text
                if str(banner_value).lower() == destination.lower():
                    print(banner_value + "Name is same as " + destination + " and this step is passed")
                else:
                    print(banner_value + "Name is same as " + destination + " and this step is failed")
            else:
                print("TO date options is not displaying and this step is failed")
        except Exception as e:
            print(str(e))

    def search_by_destination(self, destination):
        try:
            if self.driver.find_element_by_xpath(self.input_destination):
                self.driver.find_element_by_xpath(self.input_destination).send_keys(destination)
                time.sleep(2)
                self.driver.find_element_by_xpath(self.input_destination).send_keys(Keys.ENTER)
                print(destination + " is entered as destination and this step is passed")
            else:
                print("search options not displaying and this step is failed")
        except Exception as e:
            print(str(e))

    def search_by_experience(self, experience):
        try:
            if self.driver.find_element_by_xpath(self.input_experience):
                self.driver.find_element_by_xpath(self.input_experience).send_keys(experience)
                time.sleep(2)
                self.driver.find_element_by_xpath(self.input_experience).send_keys(Keys.ENTER)
                print(experience + " is entered as experience and this step is passed")
            else:
                print("search options not displaying and this step is failed")
        except Exception as e:
            print(str(e))

    def display_all_search_result(self):
        try:
            if self.driver.find_element_by_xpath(self.search_result):
                table = self.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/div[2]/div/div[2]/div[3]")
                table_row = table.find_elements_by_tag_name("h4")
                for row in table_row:
                    print("The activity in destination: " + row.text + " and this step is passed")
            else:
                print("search result is not displaying and this step is failed")
        except Exception as e:
            print(str(e))

    def use_filter_sort_by(self,sort_option):
        try:
            if self.driver.find_element_by_css_selector(self.sort_by):
                self.driver.find_element_by_css_selector(self.sort_by).click()
                print("the sort by button is clicked and this step is passed")
                time.sleep(2)
                if sort_option.lower() == "lowestprice":
                    self.driver.find_element_by_link_text("Lowest Price").click()
                    print("the sort by  lowestprice button is clicked and this step is passed")
                elif sort_option.lower() == "mostpopular":
                    self.driver.find_element_by_link_text("Most Popular").click()
                    print("the sort by  mostpopular button is clicked and this step is passed")
                else:
                    print("sort by is not correct and  this step is failed")
            else:
                print("sort by option is not displaying and  this step is failed")
        except Exception as e:
            print(str(e))

    def use_filter_price_by(self, filter_name):
        try:
            if self.driver.find_element_by_css_selector(self.filter_by_price):
                self.driver.find_element_by_css_selector(self.filter_by_price).click()
                print("Filter by price option is selected and this step is passed")
                time.sleep(2)
                if filter_name == "under50":
                    self.driver.find_element_by_xpath(self.checkbox_under_50).click()
                    print("Filter by price under 50 option is selected and this step is passed")
                elif filter_name == "50-100":
                    self.driver.find_element_by_xpath(self.checkbox_50_100).click()
                    print("Filter by price under 50-100 option is selected and this step is passed")
                elif filter_name == "100-150":
                    self.driver.find_element_by_xpath(self.checkbox_100_250).click()
                    print("Filter by price under 100-150 option is selected and this step is passed")
                elif filter_name == "over250":
                    self.driver.find_element_by_xpath(self.checkbox_over_250).click()
                    print("Filter by price under over250 option is selected and this step is passed")
                else:
                    print("filter options is not displaying and this step is failed")
        except Exception as e:
            print(str(e))

    def display_all_category(self):
        try:
            if self.driver.find_element_by_class_name("margin-xs-right").is_displayed():
                table = self.driver.find_element_by_class_name("margin-xs-right")
                table_row = table.find_elements_by_class_name("containers-Search-ParentCategoryFacetTiles-style---tileColumn")
                for row in table_row:
                    row_name = row.text
                    if row_name != "":
                        print("The category are displayed: " + row_name)
                    else:
                        pass
            else:
                print("The category option not displaying")
        except Exception as e:
            print(str(e))

    def select_category(self, category):
        try:
            if self.driver.find_element_by_class_name("margin-xs-right").is_displayed():
                table = self.driver.find_element_by_class_name("margin-xs-right")
                table_row = table.find_elements_by_class_name("containers-Search-ParentCategoryFacetTiles-style---tileColumn")
                for row in table_row:
                    row_name = row.text
                    if category in row_name:
                        row.click()
                        print("The category is displayed: " + row_name + " category is selected and this step is passed")
                        break
                    else:
                        pass
            else:
                print("The category option not displaying")
        except Exception as e:
            print(str(e))

    def display_result_for_selected_category(self):
        try:
            if self.driver.find_element_by_class_name("containers-Search-styles---activities").is_displayed():
                table = self.driver.find_element_by_class_name("containers-Search-styles---activities")
                table_row = table.find_elements_by_tag_name("h4")
                for row in table_row:
                    row_name = row.text
                    if row_name != "":
                        print("The result for selected category: " + row_name)
                    else:
                        pass
            else:
                print("The category option not displaying")
        except Exception as e:
            print(str(e))

    def select_option_from_category_result(self, category_option):
        try:
            if self.driver.find_element_by_class_name("containers-Search-styles---activities").is_displayed():
                table = self.driver.find_element_by_class_name("containers-Search-styles---activities")
                table_row = table.find_elements_by_xpath("//div[@class='padding-md-right padding-lg-bottom containers-Search-styles---mobileSearchResultsColumn']")
                for row in table_row:
                    row_name = row.text
                    if category_option in row_name:
                        row.click()
                        print(category_option+" category option selected and this step passed")
                        break
                    else:
                        pass
            else:
                print("The category option not displaying")
        except Exception as e:
            print(str(e))

    def available_days_for_booking(self):
        wait_for_page_load()
        try:
            if self.driver.find_element_by_xpath("//div[@class='components-BookingWidgetNoTickets-style---main margin-sm-v']"):
                current_date = self.driver.find_element_by_xpath("//span[@class='calendarDay    selected available']").text
                print("The Available date for this month : " + current_date)
                table = self.driver.find_element_by_xpath("//div[@class='components-BookingWidgetNoTickets-style---main margin-sm-v']")
                table_row = table.find_elements_by_xpath("//span[@class='calendarDay    available']")
                for row in table_row:
                    row_name = row.text
                    if row_name != "":
                        print("The Available date for this month : " + row_name)
                    else:
                        print("The No Available for month")
            else:
                print("Booking calendar option is not showing")
        except Exception as e:
            print(str(e))

    def select_date_from_widget(self,date):
        wait_for_page_load()
        try:
            if self.driver.find_element_by_xpath("//div[@class='month-body']"):
                table = self.driver.find_element_by_xpath("//div[@class='month-body']")
                table_row = table.find_elements_by_xpath("//div[@class='ember-view __ui-internal__calendar-day__1e941 calendar-day has-availability not-sold-out availability-style-price-range-2 clickable-days']")
                for row in table_row:
                    row_name = row.text
                    if date in row_name:
                        row.click()
                        print("The Available date for this month in widget : " + row_name)
                        break
                    else:
                        pass
            else:
                print("Booking calendar option is not showing")
        except Exception as e:
            print(str(e))

    def select_time_available_from_widget(self, time):
        wait_for_page_load()
        try:
            if self.driver.find_element_by_xpath("//div[@class='form-body']"):
                table = self.driver.find_element_by_xpath("//div[@class='form-body']")
                table_row = table.find_elements_by_xpath("//a[@class='ember-view __ui-internal__time-option__e63ce time-option is-bookable not-sold-out show-as-button']")
                for row in table_row:
                    row_name = row.text
                    if time in row_name:
                        row.click()
                        print("The Available time for this month is selected : " + row_name)
                        break
                    else:
                        pass
            else:
                print("Time option is not showing")
        except Exception as e:
            print(str(e))

    def click_book_now_button(self):
        wait_for_page_load()
        try:
            self.driver.find_element_by_class_name("components-BookingWidgetNoTickets-style---bookNowButton").click()
            print("The BOOK NOW button is clicked and this step is passed")
        except Exception as e:
            print(str(e))

    def select_number_ticket(self):
            if self.driver.find_element_by_xpath("//div[@class='ember-view pro-form-quantity']"):
                button = self.driver.find_element_by_xpath("//div[2]/div/div/div/form/div/div/div/div/div/span/a[2]")
                flag = True
                while flag == True:
                    button.click()
                    print("Increasing the number of selected tickets beyond the availability prevents me from "
                          "booking that timeslot")
                    wait_for_page_load()
                    if self.driver.find_element_by_xpath("//div[5]/div/div/form/div/div/div/div").is_displayed():
                        error_meesgae =self.driver.find_element_by_xpath("//div[5]/div/div/form/div/div/div/div").text
                        print("The error message is displaying for Increasing the number of selected tickets "
                              "beyond the availability prevents me from booking that timeslot:: " + error_meesgae)
                        flag = False
                    else:
                        flag = True
            else:
                print("Time option is not showing")
