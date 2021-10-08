from .base_page import BasePage
from .locators import ApplicationPageLocators
from selenium.webdriver.common.action_chains import ActionChains
import time


class ApplicationPage(BasePage):

    def confirm_by_reading_the_instructions(self):
        confirm_instruction = self.browser.find_element(*ApplicationPageLocators.CONFIRM_INSTRUCTION)
        confirm_instruction.click()

    def registration_information_about_the_applicant(self):
        button_apply = self.browser.find_element(*ApplicationPageLocators.BUTTON_APPLY)
        button_apply.click()
        self.should_be_button_clickable()
        button_forward = self.browser.find_element(*ApplicationPageLocators.BUTTON_FORWARD)
        button_forward.click()

    def input_child_iin(self, child_iin):
        self.should_be_input_child_iin_clickable()
        input_child_iin = self.browser.find_element(*ApplicationPageLocators.INPUT_CHILD_IIN)
        input_child_iin.send_keys(child_iin)
        action = ActionChains(self.browser)
        action.move_by_offset(100, 100).perform()
        action.click().perform()

    def input_child_name(self, child_name):
        input_child_name = self.browser.find_element(*ApplicationPageLocators.INPUT_CHILD_NAME)
        self.should_be_load_page_disappeared()
        input_child_name.send_keys(child_name)

    def application_submit(self):
        button = self.browser.find_element(*ApplicationPageLocators.BUTTON_SUBMIT)
        button.click()

    def should_be_button_clickable(self):
        self.is_element_clickable(*ApplicationPageLocators.BUTTON_FORWARD), \
            "Button forward is not presented"

    def should_be_input_child_iin_clickable(self):
        self.is_element_present(*ApplicationPageLocators.INPUT_CHILD_IIN), \
            "Input Child IIN is not clickable"

    def should_be_input_child_name_clickable(self):
        self.is_element_present(*ApplicationPageLocators.INPUT_CHILD_NAME), \
            "Input Child name is not clickable"

    def should_be_input_child_iin_is_empty(self):
        message = self.browser.find_element(*ApplicationPageLocators.MESSAGE_VALIDATION_CHILD_IIN).text
        message_expected = "Необходимо заполнить это поле."

        assert message_expected == message, \
            f"Wrong is empty text, got {message} instead of {message_expected}"

    def should_not_be_input_child_iin_is_empty(self):
        message = self.browser.find_element(*ApplicationPageLocators.MESSAGE_VALIDATION_CHILD_IIN).text
        assert len(message) == 0, \
            f"is empty text is presented, got {message}"

    def should_be_load_page_disappeared(self):
        self.is_disappeared(*ApplicationPageLocators.LOAD_PAGE, timeout=1), \
            "Load page, not disappeared"

    def should_be_success_message(self):
        message = self.browser.find_element(*ApplicationPageLocators.SUCCESS_MESSAGE).text
        message_expected = "ребенок успешно встал в очередь"

        assert message_expected in message, \
            f"Wrong success_message, got {message} instead of {message_expected}"