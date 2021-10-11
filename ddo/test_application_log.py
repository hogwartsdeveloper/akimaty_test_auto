from pages.main_page import MainPage
from pages.sso_page import SSOPage
from pages.client_page import ClientPage
from pages.application_log_page import ApplicationLogPage
import time


link = "http://10.202.19.110:5002/"
child_iin = "200726600157"
status = "в очереди"


def test_application_log(browser):
    page = MainPage(browser, link)
    page.open()
    page.warning_banner_close()
    page.go_to_login_page_client()
    sso_page = SSOPage(browser, browser.current_url)
    sso_page.log_in_client()
    client_page = ClientPage(browser, browser.current_url)
    client_page.go_to_application_log_page()

    application_log = ApplicationLogPage(browser, browser.current_url)
    application_log.should_be_application_log_table()
    application_log.search_for_application_by_child_by_iin(child_iin)
    application_log.search_for_application_by_status_queue()
    time.sleep(5)
    application_log.should_be_application()
    time.sleep(10)