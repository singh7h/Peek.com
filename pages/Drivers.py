from selenium import webdriver


def drivers(driver):
    if driver.lower() == "chrome":
        return webdriver.Chrome("/Users/harmansingh/PycharmProjects/Tesla_site/Webdriver/chromedriver")
    else:
        print("No Driver")