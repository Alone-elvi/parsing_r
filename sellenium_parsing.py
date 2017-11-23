# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# from selenium import webdriver
#
# caps = webdriver.DesiredCapabilities.FIREFOX
# caps["marionette"] = False
#
# driver = webdriver.Firefox(capabilities=caps)
#
# driver.get("http://www.google.com")
#
# print (driver.title)
#
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

url = "https://tsouz.belgiss.by/#ui-tabs-1"


def init_driver():
    driver = webdriver.Firefox()
    # driver.maximize_window()
    # driver.implicitly_wait(20)
    driver.wait = WebDriverWait(driver, 10)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    finally:
        driver.quit()
    return driver


def lookup(driver, query):
    driver.get("https://tsouz.belgiss.by/")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "q")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "btnK")))
        box.send_keys(query)
        try:
            button.click()
        except ElementNotVisibleException:
            button = driver.wait.until(EC.visibility_of_element_located(
                (By.NAME, "btnG")))
            button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")


def find_tag(driver, tag):
    finded_tag = driver.find_element_by_tag_name(tag)
    return finded_tag


def find_class(driver, class_):
    return driver.find_element_by_class_name(class_).text


def find_classes(driver, class_):
    return driver.find_elements_by_class_name(class_)


def find_id(driver, id_):
    return driver.find_element_by_id(id_)


def find_xpath(driver, xpath_):
    return driver.find_element_by_xpath(xpath_)


if __name__ == "__main__":
    xpath_string = '/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[2]/td[4]'
    css_string = 'ui-jqgrid-btable'
    # driver = init_driver()
    driver = webdriver.Firefox()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "tableCert"))
        )
    finally:
        driver.quit()

    driver.get(url)
    driver.switch_to.active_element
    # print(find_class(driver, css_string))
    print(find_id(driver, 'tableCert'))
    list_of_elems = find_xpath(driver, xpath_string)
    i = 0
    for elem in list_of_elems:
        i += 1
        print(i)
        print(elem.text)
    # // *[ @ id = "8268"]/td[4]/a

    # print(find_id(driver, 'gbox_tableCert', url).text)
    # print(find_classes(driver, 'ui-state-default', url))
    # lookup(driver, "Selenium")
    time.sleep(5)
    driver.quit()
