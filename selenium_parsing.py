# -*- coding: utf-8 -*-
import csv
import os
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# from selenium.common.exceptions import ElementNotVisibleException

url = "https://tsouz.belgiss.by/"


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


def check_url_from_csv(filename, checking_url):
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

        try:
            if tab_no[3]:
                g = tab_no[3]
        except IndexError:
            # Получить общее количество стрниц в таблице
            pages = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="sp_1_' + what_of_table + '"]'))
            )
            # Убрать пробелы из общего количества страниц в таблице и перевести в int
            g = int(''.join(((pages.get_attribute('innerHTML')).split())))

        # Ввести последнюю обработанную страницу и нажать ENTER
        go_to_page = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div["
                                            + tab_no[0] +
                                            "]/div/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input"))
        )
        go_to_page.clear()
        try:
            if tab_no[2]:
                gtp = tab_no[2]
        except IndexError:
            gtp = int(read_grab_page_position(what_of_table))
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
                # Получить элемент с атрибутом href
                el = i.get_attribute('href')
                # Обрабатывать только видимые элементиты.
                # В таблице куча скрытых элементов из соседних вкладок.
                fl = i.is_displayed()
                # Проверка, совпадает ли урл с частью общего для этой таблицы и виден ли этот элемент
                if tab_no[1] in str(el) and fl:
                    # Проверка, существует ли такой url в csv файле, если нет, то записать в csv
                    if not check_url_from_csv(what_of_table, el):
                        save_url_to_csv(what_of_table, el)
                        # returned_links.append(el)
            # Кликнуть на span для перехода на слудующую страницу
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[' + tab_no[
                0] + ']/div/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[6]/span').click()
            # Напечатать обрабатываемую страницу для себя :)
            print('Page No - ' + str(gtp + 1))
            # gtp, номер обработанной страницы. Увеличить на 1
            write_grab_page_position(what_of_table, str(gtp - 1))
            gtp += 1
            if gtp >= g:
                return 1

    except Exception as e:
        print(e)
        driver.quit()
        # Записать номер последней обработанной страницы
        try:
            if not tab_no[2] or not tab_no[3]:
                pass
        except IndexError:
            if gtp <= 0:
                gtp = int(read_grab_page_position(what_of_table))
            write_grab_page_position(what_of_table, str(gtp - 1))
        # Зпустить по новой
        take_urls_form_table(tab_no, what_of_table)


    # except TimeoutException:
    #     print("Time is out")
    #     driver.quit()
    #     # Записать номер последней обработанной страницы
    #     try:
    #         if not tab_no[2] or not tab_no[3]:
    #             pass
    #     except IndexError:
    #         if gtp <= 0:
    #             gtp = int(read_grab_page_position(what_of_table))
    #         write_grab_page_position(what_of_table, str(gtp - 1))
    #     # Зпустить по новой
    #     take_urls_form_table(tab_no, what_of_table)
    # except WebDriverException as e:
    #     print(e)
    #     driver.quit()
    #     # Записать номер последней обработанной страницы
    #     try:
    #         if not tab_no[2] or not tab_no[3]:
    #             pass
    #     except IndexError:
    #         if gtp <= 0:
    #             gtp = int(read_grab_page_position(what_of_table))
    #         write_grab_page_position(what_of_table, str(gtp - 1))
    #     # Зпустить по новой
    #     take_urls_form_table(tab_no, what_of_table)
    # except ValueError as e:
    #     driver.quit()
    #     # Записать номер последней обработанной страницы
    #     try:
    #         if not tab_no[2] or not tab_no[3]:
    #             pass
    #     except IndexError:
    #         if gtp <= 0:
    #             gtp = int(read_grab_page_position(what_of_table))
    #         write_grab_page_position(what_of_table, str(gtp - 1))
    #     # Зпустить по новой
    #     take_urls_form_table(tab_no, what_of_table)
    finally:
        #  Закрыть драйвер
        driver.quit()
        # Записать номер последней обработанной страницы
        try:
            if not tab_no[2] or not tab_no[3]:
                pass
        except IndexError:
            if gtp <= 0:
                gtp = int(read_grab_page_position(what_of_table))
            write_grab_page_position(what_of_table, str(gtp - 1))


def take_table(tab_no, what_of_table):
    urls_list = take_urls_form_table(tab_no, what_of_table)


if __name__ == "__main__":
    urls_with_ids = {
        # "tableCerttrPager": ["3", "CerttrDetailFree.php?UrlId="],
         "tableDecltrPager": ["4", "DecltrDetailFree.php?UrlId="]
    }

    for key, val in urls_with_ids.items():
        print(str(val[0]), str(key))
        take_table(val, str(key))
