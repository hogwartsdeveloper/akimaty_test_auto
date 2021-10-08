from .base_page import BasePage


class LoginBasePage(BasePage):
    def client_login_with_auth_key(self):
        self.type_user = "client"
        self.key = "AUTH_RSA256.p12"
        edk = self.signing_with_key()
        edk.login_signing_with_key()

    def employee_login_with_auth_key(self):
        self.type_user = "employee"
        self.key = "AUTH_RSA256.p12"
        edk = self.signing_with_key()
        edk.login_signing_with_key()

    def employee_login_with_rsa_key(self):
        self.type_user = "employee"
        self.key = "RSA256.p12"
        edk = self.signing_with_key()
        edk.login_signing_with_key()

    def expired_login_with_auth_key(self):
        self.type_user = "expired"
        self.key = "AUTH_RSA256.p12"
        edk = self.signing_with_key()
        edk.login_signing_with_key()