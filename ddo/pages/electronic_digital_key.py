from pywinauto import Application
from pywinauto import keyboard
from .locators import ElectronicsDigitalKeyLocators as EDK


class ElectronicsDigitalKey:
    def __init__(self, key, password):
        self.key = key
        self.password = password
        self.timeout = 5

    def signing_with_key(self):
        app_selection_key = Application(backend="uia").connect(title='Открыть файл', timeout=self.timeout)
        input_key_path = app_selection_key.ОткрытьФайл[EDK.INPUT_KEY_PATH].wrapper_object()
        input_key_path.type_keys(self.key)
        keyboard.send_keys(EDK.BUTTON_SUBMIT)

        app_key_generation = Application(backend="uia").connect(title='Формирование ЭЦП', timeout=self.timeout)
        input_key_password = app_key_generation.ФормированиеЭЦП[EDK.INPUT_PASSWORD].wrapper_object()
        input_key_password.type_keys(self.password)
        keyboard.send_keys(EDK.BUTTON_SUBMIT)
        keyboard.send_keys(EDK.BUTTON_SUBMIT)
        keyboard.send_keys(EDK.BUTTON_SUBMIT)