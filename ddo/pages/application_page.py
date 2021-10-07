from .base_page import BasePage
from .locators import ApplicationPageLocators
import time


class ApplicationPage(BasePage):

    def confirm_by_reading_the_instructions(self):
        confirm_instruction = self.browser.find_element(*ApplicationPageLocators.CONFIRM_INSTRUCTION)
        confirm_instruction.click()

    def input_child_iin(self, child_iin):
        button_apply = self.browser.find_element(*ApplicationPageLocators.BUTTON_APPLY)
        button_apply.click()
        self.should_be_button_forward()
        button_forward = self.browser.find_element(*ApplicationPageLocators.BUTTON_FORWARD)
        button_forward.click()
        self.should_be_input_clickable()
        input_child_iin = self.browser.find_element(*ApplicationPageLocators.INPUT_CHILD_IIN)
        input_child_iin.send_keys(child_iin)

    def input_child_name(self, child_name):
        input_child_name = self.browser.find_element(*ApplicationPageLocators.INPUT_CHILD_NAME)
        input_child_name.send_keys(child_name)

    def should_be_button_forward(self):
        self.is_element_present(*ApplicationPageLocators.BUTTON_FORWARD), \
            "Button forward is not presented"

    def should_be_input_clickable(self):
        self.is_element_clickable(*ApplicationPageLocators.INPUT_CHILD_IIN), \
            "Input Child IIN is not clickable"

    def should_be_input_child_iin_is_empty(self):
        message = self.browser.find_element(*ApplicationPageLocators.MESSAGE_VALIDATION_CHILD_IIN).text
        message_expected = ""

    def should_not_be_input_child_iin_is_empty(self):
        pass

    def should_be_child_age_exceed_the_norm(self):
        pass

    def should_not_be_child_age_exceed_the_norm(self):
        pass

    def should_be_child_in_queue(self):
        pass

    def should_not_child_in_queue(self):
        pass