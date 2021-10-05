from pages.main_page import MainPage
from pages.sso_page import SSOPage
from pages.client_page import ClientPage
from pages.employee_page import EmployeePage

link = "http://10.202.19.110:5002/"


def test_client_authorization_check_using_valid_edk(browser):
    page = MainPage(browser, link)
    page.open()
    page.warning_banner_close()
    page.go_to_login_page_client()
    sso_page = SSOPage(browser, browser.current_url)
    sso_page.authorization_with_the_auth_key()
    client_page = ClientPage(browser, browser.current_url)
    client_page.should_be_client_url()


def test_employee_authorization_check_using_valid_edk(browser):
    page = MainPage(browser, link)
    page.open()
    page.warning_banner_close()
    page.go_to_login_page_employee()
    sso_page = SSOPage(browser, browser.current_url)
    sso_page.login_on_behalf_of_the_employee()
    employee_page = EmployeePage(browser, browser.current_url)
    employee_page.should_be_employee_url()


def test_authorization_check_rsa_key(browser):
    page = MainPage(browser, link)
    page.open()
    page.warning_banner_close()
    page.go_to_login_page_employee()
    sso_page = SSOPage(browser, browser.current_url)
    sso_page.login_rsa()
    client_page = ClientPage(browser, browser.current_url)
    client_page.should_be_not_client_url()


def test_authorization_expired_key(browser):
    page = MainPage(browser, link)
    page.open()
    page.warning_banner_close()
    page.go_to_login_page_employee()
    sso_page = SSOPage(browser, browser.current_url)
    sso_page.login_on_behalf_of_the_experied_key()
    client_page = ClientPage(browser, browser.current_url)
    client_page.should_be_not_client_url()
