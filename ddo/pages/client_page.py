from .base_page import BasePage
from .locators import ClientPageLocators


class ClientPage(BasePage):

    def go_to_application_submission_page(self):
        application_submission_page = self.browser.find_element(*ClientPageLocators.APPLICATION_SUBMISSION)
        application_submission_page.click()

    def should_be_client_page(self):
        self.should_be_banner()
        self.should_be_client_url()

    def should_be_not_client_page(self):
        self.should_be_not_banner()
        self.should_be_not_client_url()

    def should_be_client_url(self):
        login_url = self.browser.current_url
        assert "Client" in login_url, \
            f"Wrong url, got {login_url}, instead of 'Client'"

    def should_be_not_client_url(self):
        login_url = self.url
        assert "Client" not in login_url, \
            f"Wrong url, got {login_url}"

    def should_be_banner(self):
        assert self.is_element_present(*ClientPageLocators.BANNER), "Banner is not present"

    def should_be_not_banner(self):
        assert self.is_not_element_present(*ClientPageLocators.BANNER), "Banner is present"
