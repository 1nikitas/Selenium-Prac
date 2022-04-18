import openpyxl

book = openpyxl.Workbook()
sheet = book.active

sheet.cell(row=1, column=1).value = "Направление"
sheet.cell(row=1, column=2).value = "Информация о перевозчике"
sheet.cell(row=2, column=2).value = "Информация"
sheet.cell(row=2, column=3).value = "Контакты"
sheet.cell(row=1, column=4).value = "Ставка"
sheet.cell(row=1, column=5).value = "Транспорт"
sheet.cell(row=2, column=5).value = "Информация о машине"
sheet.cell(row=2, column=6).value = "Параметры машины"
sheet.cell(row=2, column=7).value = "Габаритные размеры машины"
sheet.cell(row=1, column=8).value = "Откуда"
sheet.cell(row=2, column=8).value = "Город"
sheet.cell(row=1, column=9).value = "Куда"
sheet.cell(row=2, column=9).value = "Периодичность загрузки"
sheet.cell(row=2, column=10).value = "Возможные варианты разгрузки"



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










firm_params = browser.find_elements(By.CLASS_NAME, value="firm-params")
for firm_param in firm_params:
    info = firm_param.text.replace(",", "").split("\n")
    print(info)
    print("-"*40)



book.save("Result.xlsx")
book.close()

