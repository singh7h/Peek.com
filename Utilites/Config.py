from selenium import webdriver
import time


def driver_path(driver):
    try:
        if driver.lower() == "chrome":
            driver = webdriver.Chrome(executable_path="../Driver/chromedriver")
        return driver
    except Exception as e:
        print(str(e))


def wait_for_page_load():
    try:
        time.sleep(3)
    except Exception as e:
        print(str(e))


