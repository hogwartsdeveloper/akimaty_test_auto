from .base_page import BasePage
from .locators import EmployeePageLocators


class EmployeePage(BasePage):

    def should_be_employee_page(self):
        self.should_be_name_chapter()
        self.should_be_employee_url()

    def should_be_not_employee_page(self):
        self.should_be_not_name_chapter()
        self.should_be_not_employee_url()

    def should_be_employee_url(self):
        login_url = self.browser.current_url
        assert "Employee" in login_url, \
            f"Wrong url, got {login_url}, instead of 'Employee'"

    def should_be_not_employee_url(self):
        login_url = self.browser.current_url
        assert "Employee" not in login_url, \
            f"Wrong url, got {login_url}, instead of 'Employee'"

    def should_be_name_chapter(self):
        self.is_element_present(*EmployeePageLocators.NAME_CABINET_CHAPTER), \
            "Name chapter is not present"

    def should_be_not_name_chapter(self):
        self.is_not_element_present(*EmployeePageLocators.NAME_CABINET_CHAPTER), \
            "Name chapter is present"
