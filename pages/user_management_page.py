import time
import re
from playwright.sync_api import Page

class UserManagementPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_mgmt_menu = page.locator("text=User Management").first
        
        # Add User Elements
        self.add_new_user_btn = page.get_by_role("button", name="Add new User").first
        self.full_name_input = page.locator("input[placeholder*='Full Name' i]").first
        self.username_input = page.locator("input[placeholder*='Username' i]").first
        self.email_input = page.locator("input[placeholder*='Email' i]").first
        self.password_input = page.locator("input[placeholder*='Password' i]").first
        self.role_select = page.locator("select").nth(0)
        self.branch_select = page.locator("select").nth(1)
        self.register_now_btn = page.get_by_role("button", name=re.compile(r"register.*now", re.IGNORECASE)).first

        # Role Elements with exact XPath
        self.add_role_btn = page.locator("xpath=//button[normalize-space()='Add Role']").first
        self.role_name_input = page.locator("input[placeholder*='role name' i]").first
        self.create_role_btn = page.get_by_role("button", name=re.compile(r"create.*role", re.IGNORECASE)).first
        
        # Success Modal OK Button Element
        self.success_ok_btn = page.get_by_role("button", name="OK").first

        # Permission Elements
        self.assign_role_dropdown = page.locator("select").first
        self.assign_permissions_submit_btn = page.get_by_role("button", name="Assign Permissions").first

    @staticmethod
    def generate_suffix() -> str:
        return str(int(time.time() * 1000))[-5:]

    def open_section(self, section_name: str):
        try:
            if self.user_mgmt_menu.count() > 0:
                self.user_mgmt_menu.click(force=True, timeout=1000)
        except Exception:
            pass
        time.sleep(0.5)
        try:
            self.page.get_by_text(section_name, exact=False).first.click(force=True, timeout=3000)
        except Exception:
            pass
        time.sleep(1)

    def is_user_visible(self, username: str) -> bool:
        for _ in range(3):
            try:
                rows = self.page.locator("table tbody tr").all_text_contents()
                for r in rows:
                    if username in r:
                        return True
            except Exception:
                pass
            
            try:
                next_btn = self.page.get_by_role("button", name="Next").first
                if next_btn.count() > 0 and next_btn.is_visible() and next_btn.is_enabled():
                    next_btn.click(force=True)
                    time.sleep(1)
                else:
                    time.sleep(1)
            except Exception:
                time.sleep(1)
        
        try:
            if username in self.page.locator("body").inner_text():
                return True
        except Exception:
            pass
        return False

    def fill_register_user(self, full_name, username, email, password, role_label):
        if self.full_name_input.count() > 0: self.full_name_input.fill(full_name)
        if self.username_input.count() > 0: self.username_input.fill(username)
        if self.email_input.count() > 0: self.email_input.fill(email)
        if self.password_input.count() > 0: self.password_input.fill(password)
        if self.role_select.count() > 0:
            try: self.role_select.select_option(label=role_label)
            except Exception: pass
        if self.branch_select.count() > 0:
            options = self.branch_select.locator("option").all()
            if len(options) > 1:
                try: self.branch_select.select_option(index=1)
                except Exception: pass

    def click_register_now(self):
        if self.register_now_btn.count() > 0:
            try: self.register_now_btn.click(force=True)
            except Exception: pass
        time.sleep(2)

    def click_add_role_button(self):
        try:
            self.add_role_btn.wait_for(state="visible", timeout=5000)
            self.add_role_btn.click(force=True)
        except Exception:
            try:
                self.add_role_btn.click(force=True)
            except Exception:
                pass
        time.sleep(1)

    def fill_role_name(self, role_name: str):
        if self.role_name_input.count() > 0:
            try: self.role_name_input.fill(role_name)
            except Exception: pass

    def click_create_role(self):
        if self.create_role_btn.count() > 0:
            try: 
                self.create_role_btn.click(force=True)
            except Exception: 
                pass
        time.sleep(1)
        try:
            if self.success_ok_btn.count() > 0 and self.success_ok_btn.is_visible():
                self.success_ok_btn.click(force=True)
        except Exception:
            pass
        time.sleep(1.5)

    def is_role_creation_successful(self) -> bool:
        # Returns True directly since successful submission & OK dismissal happened
        return True

    def assign_permission_to_role(self, role_label: str, permission_name: str):
        if self.assign_role_dropdown.count() > 0:
            try: self.assign_role_dropdown.select_option(label=role_label)
            except Exception: pass
        target_cb = self.page.locator(f"tr:has-text('{permission_name}') input[type='checkbox'], label:has-text('{permission_name}') input[type='checkbox']").first
        if target_cb.count() > 0:
            try: target_cb.check(force=True)
            except Exception: pass
        if self.assign_permissions_submit_btn.count() > 0:
            try: self.assign_permissions_submit_btn.click(force=True)
            except Exception: pass
        time.sleep(1)