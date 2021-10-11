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
    APPLICATION_SUBMISSION = (By.XPATH, "//a[contains(@href, 'Instruction')]")
    APPLICATION_LOG = (By.XPATH, "//a[contains(@href, 'List')]")


class ApplicationPageLocators:
    CONFIRM_INSTRUCTION = (By.CSS_SELECTOR, ".cs")
    BUTTON_APPLY = (By.CSS_SELECTOR, ".btn-success")
    BUTTON_FORWARD = (By.CSS_SELECTOR, "input.btn-primary")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "input[value='Отправить']")
    SETUP_CONTENT = (By.CSS_SELECTOR, "step-2")
    INPUT_CHILD_IIN = (By.XPATH, "//*[@id='step-2' and not (contains(@class, 'hidden'))]//label["
                                 "@data-bind='text:_t.ChildIin']/..//input")
    LABEL_CHILD_IIN = (By.XPATH, "//label[@data-bind='text:_t.ChildIin']")
    MESSAGE_VALIDATION_CHILD_IIN = (By.XPATH, "//label[@data-bind='text:_t.ChildIin']/..//span[1]")
    INPUT_CHILD_NAME = (By.XPATH, "//label[@data-bind='text:_t.ShortChildFullName']/..//input")
    LOAD_PAGE = (By.CSS_SELECTOR, ".loader__content")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".conteiner > h3")
    BUTTON_SUCCESS_CONFIRM = (By.CSS_SELECTOR, "button.btn-primary")


class ApplicationLogPageLocators:
    APPLICATION_TABLE = (By.CSS_SELECTOR, "#gridContainer .dx-datagrid-headers")
    INPUT_CHILD_IIN = (By.XPATH, "//*[contains(@aria-label, 'Столбец ИИН ребенка')]//input")
    SELECT_STATUS = (By.XPATH, "//*[contains(@aria-label, 'Статус')]//*[@role='button']")
    STATUS_QUEUE = (By.XPATH, "//div[text() = 'В очереди']")
    APPLICATION = (By.CSS_SELECTOR, ".dx-datagrid-rowsview .dx-scrollable-container")
    APPLICATION_NO_DATA = (By.CSS_SELECTOR, ".dx-datagrid-rowsview span")
    BUTTON_DE_QUEUING = (By.XPATH, "//button[text()='Снять с очереди']")
    INPUT_REASON_DE_QUEUING = (By.CSS_SELECTOR, "textarea.form-control")
    BUTTON_SIGN_DE_QUEUING = (By.XPATH, "//*[contains(@value, 'Подписать')]")


class EmployeePageLocators:
    NAME_CABINET_CHAPTER = (By.CSS_SELECTOR, "h1")