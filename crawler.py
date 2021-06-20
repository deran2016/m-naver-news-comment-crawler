from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def crawler(URL, i):
    title = 'output_crawling_' + str(i) + '.txt'

    split_URL = URL.split('/')
    new_URL = "https://n.news.naver.com/article/comment/" + split_URL[4] + "/" + split_URL[5]

    driver = webdriver.Chrome("./chromedriver")
    driver.get(new_URL)

    time.sleep(2)

    for i in range(999):
        try:
            btn_more = driver.find_element_by_class_name("u_cbox_btn_more")
            btn_more.click()
        except:
            break

    comments = driver.find_elements_by_class_name("u_cbox_contents")

    file = open(title, 'w', encoding = 'utf-8')
    for i in comments:
        file.write(i.text + '\n\n')

    file.close