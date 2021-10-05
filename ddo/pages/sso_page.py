from .base_page import BasePage
from .locators import SSOPageLocators
import time


class SSOPage(BasePage):
    def should_be_sign_form(self):
        assert self.is_element_present(*SSOPageLocators.FORM_SIGN), \
            "Sign form is not presented"

    def should_be_sign_button(self):
        assert self.is_element_present(*SSOPageLocators.BUTTON_SELECTION_CERTIFICATE), \
            "Sign button is not presented"

    def log_in_client(self):
        button_sign = self.browser.find_element(*SSOPageLocators.BUTTON_SELECTION_CERTIFICATE)
        button_sign.click()
        self.client_signing_with_auth_key()

    def log_in_employee(self):
        button_sign = self.browser.find_element(*SSOPageLocators.BUTTON_SELECTION_CERTIFICATE)
        button_sign.click()
        self.employee_signing_with_auth_key()

    def log_in_expired_key(self):
        button_sign = self.browser.find_element(*SSOPageLocators.BUTTON_SELECTION_CERTIFICATE)
        button_sign.click()
        self.expired_signing_with_auth_key()

    def log_in_rsa_key(self):
        button_sign = self.browser.find_element(*SSOPageLocators.BUTTON_SELECTION_CERTIFICATE)
        button_sign.click()
        self.employee_signing_with_rsa_key()
