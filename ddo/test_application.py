import time

import pytest

from pages.main_page import MainPage
from pages.sso_page import SSOPage
from pages.client_page import ClientPage
from pages.application_page import ApplicationPage
from pages.application_log_page import ApplicationLogPage


link = "http://10.202.19.110:5002/"
child_iin = "200726600157"
child_name = "Zhannur"


class TestApplication:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.warning_banner_close()
        page.go_to_login_page_client()
        sso = SSOPage(browser, browser.current_url)
        sso.log_in_client()
        client_cabinet = ClientPage(browser, browser.current_url)
        client_cabinet.go_to_application_page()
        application_page = ApplicationPage(browser, browser.current_url)
        return application_page

    def test_go_to_application_page(self, setup, browser):
        application_page = setup
        application_page.confirm_by_reading_the_instructions()
        application_page.registration_information_about_the_applicant()
        application_page.input_child_name(child_name)
        application_page.input_child_iin(child_iin)
        application_page.application_submit()
        application_page.should_be_success_message()
        application_page.confirm_success_message()
        client_cabinet = ClientPage(browser, browser.current_url)
        client_cabinet.go_to_application_log_page()
        application_log_page = ApplicationLogPage(browser, browser.current_url)
        application_log_page.remove_from_queue(child_iin)