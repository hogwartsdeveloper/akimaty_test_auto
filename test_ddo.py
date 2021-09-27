from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as au
import random
import os


def authorization_employee(browser):
    file = "AUTH_RSA256_124f02d012390a48018101f9820680974dcdf40d.p12"
    button = browser.find_element(By.CSS_SELECTOR, "[href='/Employee']")
    button.click()
    button_select = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".sign-btn"))
    )
    button_select.click()
    time.sleep(0.3)
    au.typewrite(file)
    au.press("enter")
    au.typewrite("Aa123456")
    au.press("enter")
    au.press("enter")


def authorization_client(browser):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    auth_file = os.path.join(current_dir, "EDS/client/AUTH_RSA256_97b8f11b6bc188a14b5b8c9d1be44262c2cd33ab.p12")
    button = browser.find_element(By.CSS_SELECTOR, "[href='/Client']")
    button.click()
    button_select = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".sign-btn"))
    )
    button_select.click()
    time.sleep(0.3)
    au.typewrite(auth_file)
    au.press("enter")
    time.sleep(0.1)
    au.typewrite("Astana190921")
    au.press("enter")
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
    authorization_client(driver)
finally:
    time.sleep(5)
    driver.quit()
