from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_main_page(self):
        self.should_be_warning_banner()
        self.should_be_button_login_client()
        self.should_be_button_login_employee()

    def should_be_warning_banner(self):
        assert self.is_element_present(*MainPageLocators.WARNING_BANNER), \
            "Warning banner is not presented"

    def should_be_button_login_client(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_LOGIN_CLIENT), \
            "Button login client is not presented"

    def should_be_button_login_employee(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_LOGIN_EMPLOYEE), \
            "Button login employee is not presented"

    def warning_banner_close(self):
        close_button = self.browser.find_element(*MainPageLocators.BUTTON_WARNING_BANNER_CLOSE)
        close_button.click()

    def go_to_login_page_client(self):
        button_login = self.browser.find_element(*MainPageLocators.BUTTON_LOGIN_CLIENT)
        button_login.click()

    def go_to_login_page_employee(self):
        button_login = self.browser.find_element(*MainPageLocators.BUTTON_LOGIN_EMPLOYEE)
        button_login.click()