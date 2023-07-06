# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
#
# account = driver.find_element_by_css_selector("#menu-item-50 > a")
# account.click()
# time .sleep(3)
#
#
# login = driver.find_element_by_name("username")
# login.send_keys("avante02@yandex.ru")
# time .sleep(3)
# password = driver.find_element_by_id("password")
# password.send_keys("Rasul0101--22")
# time .sleep(3)
# enter = driver.find_element_by_css_selector(" p:nth-child(3) > input.woocommerce-Button.button")
# enter.click()
# time . sleep(3)
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop .click()
# driver.execute_script("window.scrollBy(0, 600);")
# time .sleep(3)
# html5 = driver.find_element_by_css_selector("#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img")
# html5 .click()
# element = driver.find_element_by_css_selector("#product-181 > div.summary.entry-summary > h1")
# element_get_text = element.text
# assert element_get_text == "HTML5 Forms"


#
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# account = driver.find_element_by_css_selector("#menu-item-50 > a")
# account.click()
# time .sleep(3)
# login = driver.find_element_by_name("username")
# login.send_keys("avante02@yandex.ru")
# time .sleep(3)
# password = driver.find_element_by_id("password")
# password.send_keys("Rasul0101--22")
# time .sleep(3)
# enter = driver.find_element_by_css_selector(" p:nth-child(3) > input.woocommerce-Button.button")
# enter.click()
# time . sleep(3)
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop .click()
# driver.execute_script("window.scrollBy(0, 400);")
# time .sleep(3)
# shop_vkladka = driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a")
# shop_vkladka .click()
# count_items = driver.find_elements_by_css_selector("#content > ul")
# if len(count_items) == 3:
#     print(" 3 товара")
# else:
#     print("Ошибка. В каталоге не 3 товара, а" + str(len(count_items)))
# time.sleep(3)
# driver.quit()



#
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# account = driver.find_element_by_css_selector("#menu-item-50 > a")
# account.click()
# time .sleep(3)
# login = driver.find_elsement_by_name("username")
# login.send_keys("avante02@yandex.ru")
# time .sleep(3)
# password = driver.find_element_by_id("password")
# password.send_keys("Rasul0101--22")
# time .sleep(3)
# enter = driver.find_element_by_css_selector(" p:nth-child(3) > input.woocommerce-Button.button")
# enter.click()
# time . sleep(3)
# login_btn.click()
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
# status_select = driver.find_element_by_css_selector("#content > form > select > option:nth-child(1)")
# status_select_standart = status_select.get_attribute("value")
# if status_select_standart == "menu_order":
#    print("Default sorting")
# else:
#     print("Выбрано другое значение:", status_select_standart)
# time.sleep(3)
# from selenium.webdriver.support.select import Select
# status_select1 = driver.find_element_by_css_selector("#content > form > select")
# select = Select(status_select1)
# select.select_by_value("price-desc")
# time.sleep(3)
# status_select2 = driver.find_element_by_css_selector("#content > form > select")
# select = Select(status_select2)
# select.select_by_value("price-desc")
# status_selector = driver.find_element_by_css_selector("select > option:nth-child(6)")
# status_selector_new = status_selector.get_attribute("value")
# if status_selector_new == "price-desc":
# print("Sort by price: high to low")
# else:
# print("Выбрано другое значение:", select)
# time.sleep(3)


# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(30)
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# account = driver.find_element_by_css_selector("#menu-item-50 > a")
# account.click()
# time .sleep(3)
# login = driver.find_elsement_by_name("username")
# login.send_keys("avante02@yandex.ru")
# time .sleep(3)
# password = driver.find_element_by_id("password")
# password.send_keys("Rasul0101--22")
# time .sleep(3)
# enter = driver.find_element_by_css_selector(" p:nth-child(3) > input.woocommerce-Button.button")
# enter.click()
# time . sleep(3)
# login_btn.click()
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
# androidbook = driver.find_element_by_xpath('//*[@id="content"]/ul/li[1]/a[1]/img')
# androidbook.click()
# bookold_p = driver.find_element_by_css_selector("div:nth-child(2) > p > del > span")
# bookold_p_text = bookold_p.text
# booknew_p = driver.find_element_by_css_selector("div:nth-child(2) > p > ins > span")
# booknew_p_text = booknew_p.text
# assert bookold_p.text == "₹600.00"
# assert booknew_p.text == "₹450.00"
# book_cov = WebDriverWait(driver, 30).until(
#   EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cov.click()
#  book_cov_close = WebDriverWait(driver, 30).until(
#    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cov_close.click()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
# Html_book = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]')
# Html_book.click()
# trashbtn = driver.find_element_by_css_selector("#wpmenucartli > a > i")
# trashbtn.click()
# summ_element = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal > td > span"), "180.00"))
# totalsumm_element = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td > strong > span"), "183.60"))


#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
# driver.execute_script("window.scrollBy(0, 600);")
# Html_book = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]')
# Html_book.click()
# time.sleep(3)
# Js_book = driver.find_element_by_xpath('//*[@id="content"]/ul/li[5]/a[2]')
# Js_book.click()
# trashbtn = driver.find_element_by_css_selector("#wpmenucartli > a > i")
# trashbtn.click()
# time.sleep(3)
# delete1book = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-remove > a")
# delete1book.click()
# undo_btn = driver.find_element_by_css_selector("div.woocommerce-message > a")
# undo_btn.click()
# quantlocator = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input")
# quantlocator.clear()
# quantlocator.send_keys("3")
# update_btn = driver.find_element_by_name("update_cart")
# update_btn.click()
# book_amount = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input")
# book_amount_text = book_amount.text
# assert book_amount_text == "3"
# coupon_btn = driver.find_element_by_css_selector(" tr:nth-child(3) > td > div > input.button")
# time.sleep(3)
# coupon_btn.click()
# element = driver.find_element_by_css_selector(" div > div.woocommerce > ul > li")
# element_get_text = element.text
# assert element_get_text == "Please enter a coupon code."


#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# Html_book = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]')
# Html_book.click()
# trashbtn = driver.find_element_by_css_selector("#wpmenucartli > a > i")
# trashbtn.click()
# proceed_check = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cart-collaterals > div > div > a")))
# proceed_check1 = driver.find_element_by_css_selector("div.cart-collaterals > div > div > a")
# proceed_check1.click()
# firstname_element = driver.find_element_by_id("billing_first_name")
# firstname_element_check = WebDriverWait(driver, 10).until(
#     EC.element_to_be_selected(firstname_element))
# firstname1 = driver.find_element_by_id("billing_first_name")
# firstname1.send_keys("Rasul")
# lastname = driver.find_element_by_id("billing_last_name")
# lastname.send_keys("Rezyapov")
# phone = driver.find_element_by_id("billing_phone_field")
# phone.send_keys("89118244177")
# country = driver.find_element_by_css_selector("#select2-drop > div")
# country.click()
# countrysearch = driver.find_element_by_css_selector("#s2id_autogen1_search")#s2id_autogen1_search
# countrysearch.send_keys("Russia")
# countrysearch1 = driver.find_element_by_css_selector("#billing_country > option:nth-child(183)")
# countrysearch1.click()
# address = driver.find_element_by_id("billing_address_1")
# address.send_keys("Nevsky Street 112")
# town = driver.find_element_by_id("billing_city")
# town.send_keys("Saint Petersburg")
# zipcode = driver.find_element_by_id("billing_postcode")
# zipcode.send_keys("192302")
# driver.execute_script("window.scrollBy(0, 600);")
# payment_btn = driver.find_element_by_id("payment_method_cheque")
# payment_btn.click()
# order_btn = driver.find_element_by_id("place_order")
# order_btn.click()
# text_Ty = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# checkpayment = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, " li.method > strong"), "Check Payments"))