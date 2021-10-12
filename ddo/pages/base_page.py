from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .electronic_digital_key import ElectronicsDigitalKey
from keys.key_data import key_data
import os


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)
        self.type_user = None
        self.key = None

    def open(self):
        self.browser.get(self.url)

    def signing_with_key(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(current_dir, f"../keys/{self.type_user}/{self.key}")
        real_path = os.path.realpath(path)
        edk = ElectronicsDigitalKey(real_path, key_data.get(f"{self.type_user}"))
        return edk

    def client_signing_with_auth_key(self):
        self.type_user = "client"
        self.key = "AUTH_RSA256.p12"
        edk = self.signing_with_key()
        edk.signing_with_key()

    def client_signing_with_rsa_key(self):
        self.type_user = "client"
        self.key = "RSA256.p12"
        edk = self.signing_with_key()
        edk.signing_with_key()

    def employee_signing_with_auth_key(self):
        self.type_user = "employee"
        self.key = "AUTH_RSA256.p12"
        edk = self.signing_with_key()
        edk.signing_with_key()

    def employee_signing_with_rsa_key(self):
        self.type_user = "employee"
        self.key = "RSA256.p12"
        edk = self.signing_with_key()
        edk.signing_with_key()

    def expired_signing_with_auth_key(self):
        self.type_user = "expired"
        self.key = "AUTH_RSA256.p12"
        edk = self.signing_with_key()
        edk.signing_with_key()

    def expired_signing_with_rsa_key(self):
        self.type_user = "expired"
        self.key = "RSA256.p12"
        edk = self.signing_with_key()
        edk.signing_with_key()

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_clickable(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((how, what))
            ).click()
        except TimeoutException:
            return False
        return True
