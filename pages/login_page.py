from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://bpocms.ptclgroup.com/MultiTenantHDS/login"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="LOG IN NOW")

    def open(self):
        self.page.goto(self.URL, wait_until="domcontentloaded")
        expect(self.username_input).to_be_visible(timeout=10000)

    def fill_username(self, username: str):
        self.username_input.fill(username)

    def fill_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()