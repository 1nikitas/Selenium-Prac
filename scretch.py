import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime

time1 = datetime.datetime.now()
browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://id.ati.su/login/?next=https%3A%2F%2Fati.su%2F")


login = browser.find_element(By.ID,  'login')
login.send_keys('kisvlev.nikita@yandex.ru')

password = browser.find_element(By.ID, 'password')
password.send_keys('ABCDabcd1234$')

button_submit = browser.find_element(By.ID, 'action-login')
button_submit.click()

time.sleep(3)

browser.get("https://trucks.ati.su/?Weight=1")

time.sleep(3)

# info = browser.find_element(by=By.CLASS_NAME, value="contacts").text
info = browser.find_elements(by = By.CLASS_NAME, value="sc-fHeRUh")


result = []

#Бондаренко Андрей Александрович, ИП Код:240846, Перевозчик, Sochi
firm_params = browser.find_elements(By.CLASS_NAME, value="firm-params")
for firm_param in firm_params:
    info = firm_param.text.replace(",", "").split("\n")
    print(info)
    print("-"*40)

print("-"*40)

#Написать +7(965)3546652, Алексей
contacts = browser.find_elements(By.CLASS_NAME, value="contact")
for contact in contacts:
    print(contact.text)
print("-"*40)
#Вместимость 15 паллет. Термописец, Режим -20+25.
notes = browser.find_elements(By.CLASS_NAME, value="note-text")
for note in notes:
    print(note.text)
print("-"*40)
# transports = browser.find_elements(By.CSS_SELECTOR, "td[data-qa='transport']")

#RUS
truck_sels = browser.find_elements(By.CSS_SELECTOR, "label[data-qa='checkbox']")
for truck_sel in truck_sels:
    if truck_sel == "Направл.":
        continue
    else:
        print(truck_sel.text)

print("-"*40)
#рефрижератор, 5 т, 38 м3, грузовик
truck_infos = browser.find_elements(By.CSS_SELECTOR, "p[data-qa='truck-info']")

for truck_info in truck_infos:
    print(truck_info.text.replace(" ", "").split(","))
print("-"*40)
#гидролифт задн., гидр.б.
truck_loadings = browser.find_elements(By.CSS_SELECTOR, "p[data-qa='truck-loading-params']")

#ДxШxВ,м
truck_dimensions = browser.find_elements(By.CSS_SELECTOR, "p[data-qa='truck-dimensions']")
for truck_dimension in truck_dimensions:
    print(truck_dimension.text)
print("-"*40)

# гидролифт задн., гидр.б.
truck_loadings = browser.find_elements(By.CSS_SELECTOR, "p[data-qa='truck-loading-params']")
for truck in truck_loadings:
    print(truck.text)
print("-"*40)

# Куда: Россия
uploadings = browser.find_elements(By.CSS_SELECTOR, "p[data-qa='main-unloading-point-name']")
for uploading in uploadings:
    print(uploading.text)
print("-"*40)

# Куда: Москва
loadings = browser.find_elements(By.CSS_SELECTOR, "p[data-qa='loading-city']")
for upload in loadings:
    print(upload.text)
print("-"*40)
# постоянно по согласию
periods = browser.find_elements(By.CSS_SELECTOR, "p[data-qa='loading-periodicity']")
for period in periods:
    print(period.text)
print("-"*40)
# 60 руб/км наличные
# 70 руб/км без НДС
rates = browser.find_elements(By.CSS_SELECTOR, "div[data-qa='rate']")
for rate in rates:
    print(rate.text)
print("-"*40)

# browser.close()
# for firm_param, contact, note in zip(firm_params, contacts, notes):
#     print(firm_param.text, "\n", contact.text, "\n", note.text)
#     print("-"*20)
# print("-"*40)



















# for i in range(5):
#     button_next = browser.find_element(By.CLASS_NAME, '_1hrJR-2-0-717')
#     button_next.click()
#     time.sleep(3)
#     info_all = browser.find_elements(by = By.CLASS_NAME, value="sc-fHeRUh")
#     for elem in info_all:
#         print(elem.text)
#     print("-" * 50)
#     print("Мы перешли на новую страницу!")
#     print("-" * 50)

time2 = datetime.datetime.now()

print(time2-time1)


# info2 = browser.find_elements(by = By.CLASS_NAME, value="sc-evcjhq")
#
# for elem in info2:
#     print(elem.text)
#     print("-"*20)
#
#

