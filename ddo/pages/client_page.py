from .base_page import BasePage


class ClientPage(BasePage):
    def should_be_client_url(self):
        login_url = self.url
        assert "Client" in login_url, \
            f"Wrong url, got {login_url}, instead of 'Client'"

    def should_be_not_client_url(self):
        login_url = self.url
        assert "Client" not in login_url, \
            f"Wrong url, got {login_url}"