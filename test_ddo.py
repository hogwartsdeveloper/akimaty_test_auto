from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as au
import random


def authorization_employee(browser):
    file = "AUTH_RSA256_124f02d012390a48018101f9820680974dcdf40d.p12"
    button = browser.find_element(By.CSS_SELECTOR, "[href='/Employee']")
    button.click()
    time.sleep(3)
    button_select = browser.find_element(By.CSS_SELECTOR, ".sign-btn")
    button_select.click()
    time.sleep(2)
    au.typewrite(file)
    au.press("enter")
    time.sleep(1)
    au.typewrite("Aa123456")
    time.sleep(1)
    au.press("enter")
    time.sleep(1)
    au.press("enter")


def create_ddo(browser):
    name_ddo = f"test_{221 * random.random()}"
    bin_ddo = "210140036017"
    number = "87772217974"

    time.sleep(2)
    link_ddo = browser.find_element(By.XPATH, "//a[contains(@href, 'DayCareList')]")
    link_ddo.click()

    button_add_ddo = browser.find_element(By.CSS_SELECTOR, "[title='Добавить строку']")
    button_add_ddo.click()







link = "http://10.202.19.110:5002/"
driver = webdriver.Chrome()

try:
    driver.get(link)
    button_log_in_as_a_client = driver.find_element(By.CSS_SELECTOR, ".btn-login:nth-child(1)")

    button_see_the_queue_number = driver.find_element(By.CSS_SELECTOR, ".btn-login:nth-child(7)")
    button_instruction = driver.find_element(By.CSS_SELECTOR, ".btn-login:nth-child(10)")
    button_language_change_to_kaz = driver.find_element(By.CSS_SELECTOR, ".langs-switcher li > a")
    button_language_change_to_ru = driver.find_element(By.CSS_SELECTOR, ".langs-switcher li:nth-child(2) > a")
    button_warning_close = driver.find_element(By.CSS_SELECTOR, ".warning-modal__close")

    button_warning_close.click()
    authorization_employee(driver)
    create_ddo(driver)
finally:
    time.sleep(10)
    driver.quit()
