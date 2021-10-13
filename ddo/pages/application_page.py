from .base_page import BasePage
from .locators import ApplicationPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import os


class ApplicationPage(BasePage):

    def confirm_by_reading_the_instructions(self):
        confirm_instruction = self.browser.find_element(*ApplicationPageLocators.CONFIRM_INSTRUCTION)
        confirm_instruction.click()

    def confirm_success_message(self):
        self.is_element_clickable(*ApplicationPageLocators.BUTTON_SUCCESS_CONFIRM)
        # button = self.browser.find_element(*ApplicationPageLocators.BUTTON_SUCCESS_CONFIRM)

    # button.click()

    def registration_information_about_the_applicant(self):
        self.is_element_clickable(*ApplicationPageLocators.BUTTON_FORWARD)
        # button_forward = self.browser.find_element(*ApplicationPageLocators.BUTTON_FORWARD)
        # button_forward.click()

    def input_child_iin(self, child_iin):
        input_child_iin = self.browser.find_element(*ApplicationPageLocators.INPUT_CHILD_IIN)
        input_child_iin.send_keys("")
        input_child_iin.send_keys(child_iin)
        action = ActionChains(self.browser)
        action.move_by_offset(100, 100).perform()
        action.click().perform()

    def input_child_name(self, child_name):
        self.should_be_load_page_disappeared()
        input_child_name = self.browser.find_element(*ApplicationPageLocators.INPUT_CHILD_NAME)
        input_child_name.send_keys(child_name)

    def application_submit(self):
        self.is_element_clickable(*ApplicationPageLocators.BUTTON_SUBMIT), \
            "Button application submit not clickable"

    def select_privilege(self):
        checkbox = self.browser.find_element(*ApplicationPageLocators.CHECKBOX_PRIVILEGE)
        checkbox.click()
        select = Select(self.browser.find_element(*ApplicationPageLocators.SELECT_PRIVILEGE_TYPE))
        select.select_by_index(4)

    def attachment_document_confirm_privilege(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, '../5002.png')
        file_path_real = os.path.realpath(file_path)
        input_file = self.browser.find_element(*ApplicationPageLocators.INPUT_DOCUMENT_CONFIRM_PRIVILEGE)
        input_file.send_keys(file_path_real)

    def should_be_load_page_disappeared(self):
        assert self.is_disappeared(*ApplicationPageLocators.LOAD_PAGE, timeout=3), \
            "Load page, not disappeared"

    def should_be_success_message_text(self):
        self.should_be_success_message()
        message = self.browser.find_element(*ApplicationPageLocators.SUCCESS_MESSAGE).text
        message_expected = "Ваш ребенок успешно встал в очередь под номером"
        assert message_expected in message, \
            f"Wrong success_message, got {message} instead of {message_expected}"

    def should_be_success_message(self):
        assert self.is_element_present(*ApplicationPageLocators.SUCCESS_MESSAGE), \
            "Success message is not present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ApplicationPageLocators.SUCCESS_MESSAGE), \
            "Success message is present"

    def should_be_confirm_document_privilege_message_text(self):
        self.should_be_confirm_document_privilege_message()
        message = self.browser.find_element(*ApplicationPageLocators.MESSAGE_CONFIRM_DOCUMENT_PRIVILEGE).text
        message_expected = "Необходимо прикрепить скан-копию документа"

        assert message_expected in message, \
            f"Wrong confirm message, got {message_expected} instead of {message}"

    def should_be_confirm_document_privilege_message(self):
        assert self.is_element_present(*ApplicationPageLocators.MESSAGE_CONFIRM_DOCUMENT_PRIVILEGE), \
            "Confirm document privilege message is not prent"

    def should_be_the_child_is_in_the_queue(self):
        message = self.browser.find_element(*ApplicationPageLocators.VALIDATION_MESSAGE_QUEUE).text
        message_expected = "Ребенок уже стоит в очереди"

        assert message_expected == message, \
            "Wrong child is not queue"

    def should_not_be_child_is_in_the_queue(self):
        assert self.is_not_element_present(*ApplicationPageLocators.VALIDATION_MESSAGE_QUEUE), \
            "Wrong child is queue"

    def should_be_the_child_age_exceed_6(self):
        assert self.is_element_present(*ApplicationPageLocators.VALIDATION_MESSAGE_AGE), \
            "Validation message age is not present"

    def should_not_be_child_age_exceed_6(self):
        assert self.is_not_element_present(*ApplicationPageLocators.VALIDATION_MESSAGE_AGE), \
            "Validation message age is present"

    def should_be_verification_required_fields(self):
        message = self.browser.find_element(*ApplicationPageLocators.VALIDATION_MESSAGE_CHILD_IIN).text
        message_expected = "Необходимо заполнить это поле."

        assert message_expected == message, \
            f"Wrong validation required fields text, got {message} instead of {message_expected}"

    def should_be_verification_message_incorrect_iin(self):
        message = self.browser.find_element(*ApplicationPageLocators.VALIDATION_MESSAGE_CHILD_IIN).text
        message_expected = "ИИН, который вы ввели, некорректен"

        assert message_expected == message, \
            f"Wrong validation incorrect iin text, got {message} instead of {message_expected}"

    def should_be_application_page(self):
        self.should_be_child_iin()
        self.should_be_child_name()
        self.should_be_checkbox_privilege()
        self.should_be_button_application_submit()

    def should_be_child_iin(self):
        assert self.is_element_present(*ApplicationPageLocators.INPUT_CHILD_IIN), \
            "Child IIN is not present"

    def should_be_child_name(self):
        assert self.is_element_present(*ApplicationPageLocators.INPUT_CHILD_IIN), \
            "Child name is not present"

    def should_be_checkbox_privilege(self):
        assert self.is_element_present(*ApplicationPageLocators.CHECKBOX_PRIVILEGE), \
            "Checkbox privilege is not present"

    def should_be_button_application_submit(self):
        assert self.is_element_present(*ApplicationPageLocators.BUTTON_SUBMIT), \
            "Button application submit is not present"
