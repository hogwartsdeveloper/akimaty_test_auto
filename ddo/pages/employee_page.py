from .base_page import BasePage


class EmployeePage(BasePage):
    def should_be_employee_url(self):
        login_url = self.url
        assert "Employee" in login_url, \
            f"Wrong url, got {login_url}, instead of 'Employee'"