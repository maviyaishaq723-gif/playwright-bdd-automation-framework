import time
import random
import re
from playwright.sync_api import Page

class RidersPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Sidebar Navigation
        self.rider_list_sidebar = page.locator("a:has-text('Rider List'), li:has-text('Rider List'), a:has-text('Riders')").first
        
        # Header Action Button
        self.add_new_rider_btn = page.locator("a:has-text('Add New Rider'), button:has-text('Add New Rider')").first
        
        # Form Locators
        self.rider_name_input = page.locator("input[placeholder*='rider name' i]").first
        self.branch_select = page.locator("select").first
        
        # Phone placeholder has '03', CNIC placeholder has hyphens '-'
        self.phone_input = page.locator("input[placeholder*='03']").first
        self.cnic_input = page.locator("input[placeholder*='-']").first
        
        self.password_input = page.locator("input[placeholder*='password' i]").first
        self.create_rider_btn = page.get_by_role("button", name=re.compile(r"create.*rider", re.IGNORECASE)).first
        
        # Popup Success Button
        self.success_ok_btn = page.get_by_role("button", name="OK").first

    @staticmethod
    def generate_random_data():
        suffix = str(int(time.time() * 1000))[-4:]
        name = f"Rider_{suffix}"
        
        # Exact 11-digit Phone Number (03XXXXXXXXX)
        phone = f"0300{random.randint(1000000, 9999999)}"
        
        # Formatted CNIC with hyphens (XXXXX-XXXXXXX-X)
        p1 = f"{random.randint(30000, 39999)}"
        p2 = f"{random.randint(1000000, 9999999)}"
        p3 = f"{random.randint(1, 9)}"
        cnic_formatted = f"{p1}-{p2}-{p3}"
        
        password = f"Pass@{suffix}"
        return name, phone, cnic_formatted, password

    def navigate_to_rider_list(self):
        if self.rider_list_sidebar.is_visible():
            self.rider_list_sidebar.click()
            time.sleep(1.5)

    def click_add_new_rider_button(self):
        if self.add_new_rider_btn.is_visible():
            self.add_new_rider_btn.click()
            time.sleep(1.5)

    def fill_rider_form(self, name: str, phone: str, cnic: str, password: str):
        self.rider_name_input.wait_for(state="visible", timeout=10000)
        self.rider_name_input.fill(name)
        
        # Select Branch Dropdown
        if self.branch_select.count() > 0:
            options = self.branch_select.locator("option").all()
            if len(options) > 1:
                self.branch_select.select_option(index=1)

        # Phone input fill
        self.phone_input.click()
        self.phone_input.fill("")
        self.phone_input.press_sequentially(phone, delay=40)

        # CNIC input fill with proper hyphens
        self.cnic_input.click()
        self.cnic_input.fill("")
        self.cnic_input.press_sequentially(cnic, delay=40)

        # Password input fill
        self.password_input.fill(password)
        time.sleep(1)

    def click_create_rider(self):
        self.create_rider_btn.click(force=True)
        time.sleep(1.5)
        
        try:
            if self.success_ok_btn.is_visible(timeout=4000):
                self.success_ok_btn.click(force=True)
                time.sleep(1)
        except Exception:
            pass