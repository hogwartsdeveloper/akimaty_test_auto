from pages.main_page import MainPage
from pages.sso_page import SSOPage
from pages.client_page import ClientPage
from pages.application_page import ApplicationPage
import time


link = "http://10.202.19.110:5002/"


def test_go_to_application_page(browser):
    child_iin = "980919451129"
    child_name = "Zhannur"
    page = MainPage(browser, link)
    page.open()
    page.warning_banner_close()
    page.go_to_login_page_client()
    sso_page = SSOPage(browser, browser.current_url)
    sso_page.log_in_client()
    client_page = ClientPage(browser, browser.current_url)
    client_page.go_to_application_submission_page()
    application_page = ApplicationPage(browser, browser.current_url)
    application_page.confirm_by_reading_the_instructions()
    application_page.queuing_up_a_child(child_iin, child_name)
    time.sleep(5)