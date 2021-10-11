from pages.main_page import MainPage
from pages.sso_page import SSOPage


link = "http://10.202.19.110:5002/"


def test_application_log(browser):
    page = MainPage(browser, link)
    page.open()
    page.warning_banner_close()
    page.go_to_login_page_client()
    sso_page = SSOPage(browser, browser.current_url)
    sso_page.log_in_client()