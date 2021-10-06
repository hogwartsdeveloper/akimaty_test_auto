from .base_page import BasePage
from .locators import ApplicationPageLocators


class ApplicationPage(BasePage):

    def confirm_by_reading_the_instructions(self):
        confirm_instruction = self.browser.find_element(*ApplicationPageLocators.CONFIRM_INSTRUCTION)
        confirm_instruction.click()

    def queuing_up_a_child(self):
        pass

