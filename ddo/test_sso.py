import pytest
import allure

from pages.main_page import MainPage
from pages.sso_page import SSOPage
from pages.client_page import ClientPage
from pages.employee_page import EmployeePage

link = "http://10.202.19.110:5002/"


@allure.feature("Авторизация")
class TestAuthorization:

    @allure.story("Проверка авторизация от имени клиента")
    def test_client_log_in(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.warning_banner_close()
        page.go_to_login_page_client()
        sso_page = SSOPage(browser, browser.current_url)
        sso_page.log_in_client()
        client_page = ClientPage(browser, browser.current_url)
        client_page.should_be_client_page()

    @allure.story("Проверка авторизация от имени сотрудника")
    def test_employee_log_in(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.warning_banner_close()
        page.go_to_login_page_employee()
        sso_page = SSOPage(browser, browser.current_url)
        sso_page.log_in_employee()
        employee_page = EmployeePage(browser, browser.current_url)
        employee_page.should_be_employee_page()

    @allure.story("Проверка авторизация ключом RSA")
    @pytest.mark.xfail
    def test_client_log_in_rsa_key(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.warning_banner_close()
        page.go_to_login_page_client()
        sso_page = SSOPage(browser, browser.current_url)
        sso_page.log_in_rsa_key()
        client_page = ClientPage(browser, browser.current_url)
        client_page.should_be_not_client_page()

    @allure.story("Проверка авторизация ключом c истекшим сроком")
    def test_log_in_expired_key(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.warning_banner_close()
        page.go_to_login_page_client()
        sso_page = SSOPage(browser, browser.current_url)
        sso_page.log_in_expired_key()
        client_page = ClientPage(browser, browser.current_url)
        client_page.should_be_not_client_page()
