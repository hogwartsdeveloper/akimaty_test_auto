from selenium.common.exceptions import NoSuchElementException
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
        edk.signing_with_key()

    def client_signing_with_auth_key(self):
        self.type_user = "client"
        self.key = "AUTH_RSA256.p12"
        self.signing_with_key()

    def client_signing_with_rsa_key(self):
        self.type_user = "client"
        self.key = "RSA256.p12"
        self.signing_with_key()

    def employee_signing_with_auth_key(self):
        self.type_user = "employee"
        self.key = "AUTH_RSA256.p12"
        self.signing_with_key()

    def employee_signing_with_rsa_key(self):
        self.type_user = "employee"
        self.key = "RSA256.p12"
        self.signing_with_key()

    def expired_signing_with_auth_key(self):
        self.type_user = "expired"
        self.key = "AUTH_RSA256.p12"
        self.signing_with_key()

    def expired_signing_with_rsa_key(self):
        self.type_user = "expired"
        self.key = "RSA256.p12"
        self.signing_with_key()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True