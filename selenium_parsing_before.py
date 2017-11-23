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

import csv
import os
import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

url = "https://tsouz.belgiss.by/"


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


def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return JQuery.active")
    except WebDriverException:
        pass


def find_choise_select(webdriver, str_xpath, elems):
    # select_t = WebDriverWait(driver, 30).until(
    #     driver.find_element_by_xpath((str_xpath))
    # )
    time.sleep(10)
    select_t = webdriver.find_element_by_xpath(str_xpath)
    for option in select_t.find_elements_by_tag_name('option'):
        if option.text == str(elems):
            option.click()  # select() in earlier versions of webdriver
            break


# def get_info_from_page(url, page):
#     row_on_page = 50
#     t_row = row_on_page + 1
#     xpath_string = '/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[' + str(
#         t_row) + ']/td[4]'
#     # xpath_string = '//*[@id="rs_mtableCert"]'
#     xpath_string_t = '//*[@id="tableCert"]'
#     partial_link_text = 'CertDetailFree.php?UrlId='
#     css_string = 'ui-jqgrid-btable'
#     select_xpath_string = '/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[8]/select'
#     # driver = init_driver()
#
#     # time.sleep(10)
#     try:
#         driver.execute_script("return jQuery.active == 0")
#         for i in page:
#             element_t = WebDriverWait(driver, 30).until(
#                 EC.presence_of_element_located((By.XPATH, xpath_string_t))
#             )
#             # element = WebDriverWait(driver, 50).until(
#             #     EC.presence_of_element_located((By.ID, "8067"))
#             # )
#
#             # driver.implicitly_wait(5)
#             # element = WebDriverWait(driver, 30).until(
#             #     EC.presence_of_element_located((By.XPATH, xpath_string))
#             # )
#             # element = WebDriverWait(driver, 30).until(
#             #     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, partial_link_text))
#             # )
#             # for i in range(2):
#             #     element = WebDriverWait(driver, 10).until(ajax_complete, "Загрузка")
#             #
#             #     # element = WebDriverWait(driver, 100).until(
#             #     #     EC.presence_of_element_located((By.XPATH, xpath_string))
#             #     # )
#             #     # time.sleep(10)
#             #     # element_t = WebDriverWait(driver, 40).until(
#             #     #     EC.presence_of_element_located((By.XPATH, xpath_string_t))
#             #     # )
#             #
#             #     # print(element.get_attribute('innerHTML'))
#             #     # print(element_t.get_attribute('innerHTML'))
#             #     print(a)
#             #     print(i)
#
#     except TimeoutException:
#         print("Time is out")
#     except WebDriverException as e:
#         print(e)
#     finally:
#         driver.quit()
#     return element_t
def read_grab_page_position(filename):
    try:
        if not os.path.exists(filename + ".txt"):
            with open(filename + ".txt", "w", newline="") as file:
                file.write('0')

        with open(filename + ".txt", "r", newline="") as file:
            position = file.read()
            return position

    except Exception as e:
        print(e)
    except IOError as e:
        print("Error " + str(e) + ". Can`t access file " + filename + ".txt")


def write_grab_page_position(filename, position):
    try:
        with open(filename + ".txt", "w", newline="") as file:
            file.write(str(position))

    except Exception as e:
        print(e)
    except IOError as e:
        print("Error " + str(e) + ". Can`t access file " + filename + ".txt")


def save_url_to_csv(filename, checking_url):
    try:
        with open(filename + ".csv", "a", newline="") as file:
            writer = csv.writer(file)
            s = []
            s.append(checking_url)
            # print(s)
            writer.writerow(s)
    except Exception as e:
        print(e)


def check_url(filename, checking_url):
    # print(checking_url, file_name + ".csv")
    try:
        if not os.path.exists(filename + ".csv"):
            with open(filename + ".csv", "w", newline="") as file:
                return False

        with open(filename + ".csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if checking_url in row[0]:
                    return True

    except Exception as e:
        print(e)
    except IOError as e:
        print("Can`t access file " + filename + ".csv")
    return False


def take_urls_form_table(tab_no, what_of_table):
    driver = webdriver.Firefox()
    # driver.implicitly_wait(10)  # seconds
    driver.get(url)
    # driver.maximize_window()
    # Номер обработанной страницы. Записывается в файл, для того, чтобы при вылете начать с неё
    gtp = 0

    try:
        # Здесь я кликаю на вкладку с нужной таблицей, например
        # Сертификат ТР или Декларация ТР. xpath берётся из страницы.
        # tab_no[0] - Номер нужной таблицы
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/ul/li[' + tab_no[0] + ']/a').click()
        # Дождаться загрузки Ajax
        driver.execute_script("return jQuery.active == 0")
        # Если не включить ожидание, драйвер не ждёт и вылетает
        time.sleep(15)

        # Получить общее количество стрниц в таблице
        pages = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sp_1_' + what_of_table + '"]'))
        )
        # Убрать пробелы из общего количества страниц в таблице и перевести в int
        g = int(''.join(((pages.get_attribute('innerHTML')).split())))

        print(g)
        # Ввести последнюю обработанную страницу и нажать ENTER
        go_to_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div["
                                            + tab_no[0] +
                                            "]/div/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input"))
        )

        go_to_page.clear()
        gtp = int(read_grab_page_position(what_of_table))
        print(gtp)
        go_to_page.send_keys(str(gtp))
        go_to_page.send_keys(Keys.ENTER)
        # --------------------------------------------------------
        # Дождаться загрузки Ajax
        # driver.execute_script("return jQuery.active == 0")
        # areAjaxRequestsCompleted = driver.execute_script("return (typeof($) === 'undefined') ? true : !$.active;")

        # Дождаться загрузки Ajax
        driver.execute_script("return jQuery.active == 0")

        # g = int(pages.get_attribute('innerHTML'))
        time.sleep(10)
        # Обработка url страницы
        for ii in range(g - gtp):
            driver.execute_script("return jQuery.active == 0")
            time.sleep(10)

            # Получаем аттрибуты тега a и записываем их все в список
            list_links = driver.find_elements_by_tag_name('a')
            #  Идём по элемнтам списка, тех, у кого атрибут href
            for i in list_links:
                # print(i.get_attribute('href'))
                # Получить элемент с атрибутом href
                el = i.get_attribute('href')
                # Обрабатывать только видимые элементиты.
                # В таблице куча скрытых элементов из соседних вкладок.
                fl = i.is_displayed()
                # print(i.get_attribute('innerHTML'))
                # Проверка, совпадает ли урл с частью общего для этой таблицы и виден ли этот элемент
                if tab_no[1] in str(el) and fl:
                    # Проверка, существует ли такой url в csv файле, если нет, то записать в csv
                    if not check_url(what_of_table, el):
                        # print(fl, str(el))
                        save_url_to_csv(what_of_table, el)
                        # returned_links.append(el)
            # Кликнуть на span для перехода на слудующую страницу
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[' + tab_no[
                0] + ']/div/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[6]/span').click()
            # Напечатать обрабатываемую страницу для себя :)
            print('Page No - ' + str(gtp + 1))
            # gtp, номер обработанной страницы. Увеличить на 1
            gtp += 1
            if gtp >= g:
                return 1
                # # find_choise_select(driver, select_xpath_string, row_on_page)
                # pages = WebDriverWait(driver, 30).until(
                #     EC.presence_of_element_located((By.XPATH, '//*[@id="sp_1_tableCertPager"]'))
                # )

    except TimeoutException:
        print("Time is out")
    except WebDriverException as e:
        print(e)
        driver.quit()
        # Записать номер последней обработанной страниы
        write_grab_page_position(what_of_table, str(gtp))
        take_urls_form_table(tab_no, what_of_table)
    finally:
        #  Закрыть драйвер
        driver.quit()
        # Записать номер последней обработанной страниы
        write_grab_page_position(what_of_table, str(gtp))


def take_table(table_tag, end_page_id):
    filename = end_page_id + ".csv"

    urls_list = take_urls_form_table(table_tag, end_page_id)
    # try:
    #     with open(filename, "w", newline="") as file:
    #         writer = csv.writer(file)
    #         for ii in urls_list:
    #             print(ii)
    #             writer.writerow([ii])
    # except Exception as e:
    #     print(e)
    # finally:
    #     pass
    # print(get_urls_form_table())


if __name__ == "__main__":
    # select = driver.find_element_by_xpath(
    #     '/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[6]/span')
    # for i in select:
    #     i.click()
    #     page_info=get_info_from_page(url, i)
    #     print(page_info.get_attribute('innerHTML'))

    urls_with_ids = {
        "tableCerttrPager": ["3", "CerttrDetailFree.php?UrlId="],
        "tableDecltrPager": ["4", "DecltrDetailFree.php?UrlId="]
    }

    for key, val in urls_with_ids.items():
        print(str(val[0]), str(key))
        take_table(val, str(key))
