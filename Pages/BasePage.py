"""
Author Harman Singh
Followed the PEP standards for python
Below class is BasePage class which will inherited by all other Page class
"""
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """
        This function will open the url in browser and maximize it
        :param url:
        :return:
        """
        try:
            if url != "":
                self.driver.maximize_window()
                self.driver.get(url)
                print(url + " : url is opened")
            else:
                print("Please enter valid url")
        except Exception as e:
            print(str(e))

    def type_text(self, element, text):
        """
        This function will type the text in textbox
        :param element:
        :param text:
        :return:
        """
        try:
            if element.is_displayed():
                element.clear()
                element.send_keys(text)
                print(text + " is added to textbox")
            else:
                print(element + " is not displaying")
        except Exception as e:
            print(str(e))


