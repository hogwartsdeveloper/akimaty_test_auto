from selenium.webdriver.common.by import By


class ElectronicsDigitalKeyLocators:
    INPUT_KEY_PATH = "MenuItem"
    INPUT_PASSWORD = "TitleBar"
    BUTTON_SUBMIT = "{ENTER}"


class SSOPageLocators:
    FORM_SIGN = (By.CSS_SELECTOR, ".form")
    BUTTON_SELECTION_CERTIFICATE = (By.CSS_SELECTOR, ".sign-btn")


class MainPageLocators:
    WARNING_BANNER = (By.CSS_SELECTOR, ".warning-modal__inner")
    BUTTON_WARNING_BANNER_CLOSE = (By.CSS_SELECTOR, ".warning-modal__close")
    BUTTON_LOGIN_CLIENT = (By.CSS_SELECTOR, "a[href='/Client']")
    BUTTON_LOGIN_EMPLOYEE = (By.CSS_SELECTOR, "a[href='/Employee']")


class ClientPageLocators:
    BANNER = (By.CSS_SELECTOR, "h1")
    APPLICATION_SUBMISSION = (By.CSS_SELECTOR, ".service__title")


class ApplicationPageLocators:
    CONFIRM_INSTRUCTION = (By.CSS_SELECTOR, ".cs")
    BUTTON_APPLY = (By.CSS_SELECTOR, "")


class EmployeePageLocators:
    NAME_CABINET_CHAPTER = (By.CSS_SELECTOR, "h1")