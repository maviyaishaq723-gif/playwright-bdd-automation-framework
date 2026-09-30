import time
import re
from playwright.sync_api import Page

class PaymentModesPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Sidebar Navigation
        self.payment_modes_sidebar = page.locator("a:has-text('Payment Modes'), li:has-text('Payment Modes')").first
        
        # Header Action Button
        self.add_payment_mode_btn = page.locator("a:has-text('Add Payment Mode'), button:has-text('Add Payment Mode')").first
        
        # Form Locators
        self.payment_mode_name_input = page.locator("input[placeholder*='payment mode name' i]").first
        self.status_select = page.locator("select").first
        self.create_payment_mode_btn = page.get_by_role("button", name=re.compile(r"create.*payment.*mode", re.IGNORECASE)).first
        
        # Popup Success Button
        self.success_ok_btn = page.get_by_role("button", name="OK").first

    @staticmethod
    def generate_suffix() -> str:
        return str(int(time.time() * 1000))[-5:]

    def navigate_to_payment_modes(self):
        if self.payment_modes_sidebar.is_visible():
            self.payment_modes_sidebar.click()
            time.sleep(1.5)

    def click_add_payment_mode_button(self):
        if self.add_payment_mode_btn.is_visible():
            self.add_payment_mode_btn.click()
            time.sleep(1.5)

    def fill_payment_mode_form(self, mode_name: str):
        self.payment_mode_name_input.wait_for(state="visible", timeout=10000)
        self.payment_mode_name_input.fill(mode_name)

    def click_create_payment_mode(self):
        self.create_payment_mode_btn.click(force=True)
        time.sleep(1)
        try:
            if self.success_ok_btn.is_visible(timeout=3000):
                self.success_ok_btn.click(force=True)
        except Exception:
            pass
        time.sleep(1.5)