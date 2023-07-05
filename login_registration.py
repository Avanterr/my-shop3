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
element = driver.find_element_by_css_selector(" li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a") # нашли элемент по составному селектору
element_get_text = element.text
assert element_get_text == "Logout"