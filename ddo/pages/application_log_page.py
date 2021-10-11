import time

from .base_page import BasePage
from .locators import ApplicationLogPageLocators


class ApplicationLogPage(BasePage):

    def remove_from_queue(self, child_iin):
        self.should_be_application_log_table()
        self.search_for_application_by_child_by_iin(child_iin)
        self.search_for_application_by_status_queue()
        self.should_be_application()
        self.de_queuing()
        self.client_signing_with_rsa_key()

    def search_for_application_by_child_by_iin(self, child_iin):
        input_iin = self.browser.find_element(*ApplicationLogPageLocators.INPUT_CHILD_IIN)
        input_iin.send_keys(child_iin)

    def search_for_application_by_status_queue(self):
        select = self.browser.find_element(*ApplicationLogPageLocators.SELECT_STATUS)
        select.click()
        status_queue = self.browser.find_element(*ApplicationLogPageLocators.STATUS_QUEUE)
        status_queue.click()

    def de_queuing(self):
        time.sleep(2)
        application = self.browser.find_element(*ApplicationLogPageLocators.APPLICATION)
        application.click()
        self.is_element_clickable(*ApplicationLogPageLocators.BUTTON_DE_QUEUING)
        button = self.browser.find_element(*ApplicationLogPageLocators.BUTTON_DE_QUEUING)
        button.click()
        time.sleep(2)
        input_reason = self.browser.find_element(*ApplicationLogPageLocators.INPUT_REASON_DE_QUEUING)
        input_reason.send_keys("Test")
        time.sleep(2)
        button_sign = self.browser.find_element(*ApplicationLogPageLocators.BUTTON_SIGN_DE_QUEUING)
        button_sign.click()

    def should_be_application(self):
        self.is_element_present(*ApplicationLogPageLocators.APPLICATION), \
            "Application is not present"

    def should_not_be_application(self):
        no_data = self.browser.find_element(*ApplicationLogPageLocators.APPLICATION_NO_DATA).get_attribute("class")
        assert "dx-hidden" not in no_data, \
            "Application is present"

    def should_be_application_log_table(self):
        self.is_element_present(*ApplicationLogPageLocators.APPLICATION_TABLE), \
            "Application table is not presented"
