import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)

account = driver.find_element_by_css_selector("#menu-item-50 > a")
account.click()
time .sleep(3)


login = driver.find_element_by_name("username")
login.send_keys("avante02@yandex.ru")
time .sleep(3)
password = driver.find_element_by_id("password")
password.send_keys("Rasul0101--22")
time .sleep(3)
enter = driver.find_element_by_css_selector(" p:nth-child(3) > input.woocommerce-Button.button")
enter.click()
time . sleep(3)
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop .click()
status_select = driver.find_element_by_css_selector("#content > form > select > option:nth-child(1)")
status_select_standart = status_select.get_attribute("value")
if status_select_standart == "menu_order":
    print("Default sorting")
else:
    print("Выбрано другое значение:", status_select_standart)
    time .sleep(3)
from selenium.webdriver.support.select import Select
status_select = driver.find_element_by_css_selector("#content > form > select")
select = Select(status_select)
select.select_by_value("price-desc")
time.sleep(3)
status_select2 = driver.find_element_by_css_selector("#content > form > select")

status_select2_new = status_select.get_attribute("value")
if status_select_standart == "[price-desc]":
    print("Sort by price: high to low")
else:
    print("Выбрано другое значение:", status_select2_new)
    time .sleep(3)