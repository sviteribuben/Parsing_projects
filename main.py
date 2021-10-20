# Necessary imports
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


def get_source_html(url):
    ''' creating chromedriver (/ or something else)
    find necessary elements in the page
    and save the page comntent
    :param url:
    :return:
    '''

    driver = webdriver.Chrome(
        executable_path='C:/Users/svtrbbn/PycharmProjects/scrapy_cosmet/chromedriver.exe')

    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)

        while True:
            find_more_elements = driver.find_element_by_class_name("catalog-button-showMore")
            if driver.find_elements_by_class_name("hasmore-text"):
                with open("C:/Users/svtrbbn/PycharmProjects/scrapy_cosmet/source-page2.html", "w", encoding="utf-8") as file:
                    file.write(driver.page_source)

                break
            else:
                # создаем объект цепочки
                action = ActionChains(driver)
                action.move_to_element(find_more_elements).perform()
                time.sleep(3)

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def get_items_urls(file_path):
    with open(file_path) as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    items_divs = soup.find_all("div", class_="service-description")

    urls = []
    for item in items_divs:
        item_url = item.find("div", class_="H3").find("a").get("href")
        urls.append(item_url)

    with open("C:/Users/svtrbbn/PycharmProjects/scrapy_cosmet/urls.txt", "w ", encoding="cp437") as file:
        for url in urls:
            file.write(f'{url}\n')


    return urls
    # return "[INFO] urls successfully collect"



def main():
    print(get_items_urls(file_path="C:/Users/svtrbbn/PycharmProjects/scrapy_cosmet/source-page2.html"))

if __name__ == "__main__":
    main()

# 1) Collect all links
