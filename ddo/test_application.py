import pytest
import allure

from pages.main_page import MainPage
from pages.sso_page import SSOPage
from pages.client_page import ClientPage
from pages.application_page import ApplicationPage

link = "http://10.202.19.110:5002/"
child_name = "Zhannur"


@allure.feature("Подача заявления")
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
        application_page.confirm_by_reading_the_instructions()
        application_page.confirm_success_message()
        application_page.registration_information_about_the_applicant()
        return application_page

    @pytest.mark.skip
    @allure.story("Проверка успешной постановки ребенка в очередь ДДО")
    @allure.story("Проверка постановки в очередь ребенка который зачислен в ДДО")
    @pytest.mark.parametrize('iin', ['160124603644', '190411506142'])
    def test_verify_for_successful_queuing(self, setup, iin):
        application_page = setup
        application_page.input_child_name(child_name)
        application_page.input_child_iin(iin)
        application_page.should_not_be_child_is_in_the_queue()
        application_page.application_submit()
        application_page.client_signing_with_rsa_key()
        application_page.should_be_success_message()

    @pytest.mark.skip
    @allure.story("Проверка повторной постановке ребенка в очередь")
    @pytest.mark.parametrize('iin', ['180407603349'])
    def test_verify_re_queuing(self, setup, iin):
        application_page = setup
        application_page.input_child_name(child_name)
        application_page.input_child_iin(iin)
        application_page.should_be_the_child_is_in_the_queue()
        application_page.application_submit()
        application_page.should_not_be_success_message()

    @pytest.mark.skip
    @allure.story("Проверка постановки ребенка с возрастом 7 лет на начало учебного года")
    @pytest.mark.parametrize('iin', ['140219504440'])
    def test_verify_queue_of_a_child_7_year(self, setup, iin):
        application_page = setup
        application_page.input_child_name(child_name)
        application_page.input_child_iin(iin)
        application_page.should_be_the_child_age_exceed_6()
        application_page.application_submit()
        application_page.should_not_be_success_message()

    @pytest.mark.skip
    @allure.story("Проверка успешной постановки ребенка с льготности в очередь ДДО")
    @pytest.mark.parametrize('iin', ['200806601487'])
    def test_verify_queue_with_privilege(self, setup, iin):
        application_page = setup
        application_page.input_child_iin(iin)
        application_page.input_child_name(child_name)
        application_page.select_privilege()
        application_page.attachment_document_confirm_privilege()
        application_page.application_submit()
        application_page.client_signing_with_rsa_key()
        application_page.should_be_success_message()

    @pytest.mark.skip
    @allure.story("Проверка постановки ребенка с льготности без подтверждающий документа в очеред ДДО")
    @pytest.mark.parametrize('iin', ['200726600157'])
    def test_verify_queue_with_privilege_without_a_supporting_document(self, setup, iin):
        application_page = setup
        application_page.input_child_iin(iin)
        application_page.input_child_name(child_name)
        application_page.select_privilege()
        application_page.should_not_be_child_is_in_the_queue()
        application_page.application_submit()
        application_page.should_be_confirm_document_privilege_message()

    @allure.story("Проверка подачи заявления без заполнения обязательных полей")
    def test_verify_queue_without_filing_in_the_required_fields(self, setup):
        application_page = setup
        application_page.application_submit()
        application_page.should_be_verification_required_fields()

    @pytest.mark.skip
    @allure.story("Проверка ввода некорректного иин ребенка при постановке в очередь")
    def test_verify_queue_the_input_of_a_incorrect_iin(self, setup):
        application_page = setup
        application_page.input_child_iin("1231231311")
        application_page.application_submit()
        application_page.should_be_verification_message_incorrect_iin()
