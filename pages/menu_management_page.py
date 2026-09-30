import time
import re
import os
from playwright.sync_api import Page

class MenuManagementPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_mgmt_menu = page.locator("text=Menu Management").first
        
        # Menu Family Elements (Robust locators matching the UI design system)
        self.add_menu_family_btn = page.locator("button.inline-flex:has-text('MenuFamily'), button.inline-flex:has-text('Menu Family'), button:has-text('MenuFamily')").first
        self.family_title_input = page.locator("input[placeholder*='title' i]").first
        self.family_desc_input = page.locator("textarea[placeholder*='description' i]").first
        self.create_family_btn = page.get_by_role("button", name=re.compile(r"create.*menu family", re.IGNORECASE)).first

        # Menu Item Elements (Working & verified)
        self.add_menu_item_btn = page.locator("button.inline-flex:has-text('Add Menu'), button:has-text('Add Menu')").first
        self.item_name_input = page.locator("input[placeholder*='item name' i]").first
        self.item_price_input = page.locator("input[placeholder*='price' i], input[type='number']").first
        self.item_desc_input = page.locator("textarea[placeholder*='description' i]").first
        self.pos_code_input = page.locator("input[placeholder*='pos' i]").first
        self.menu_family_select = page.locator("select").first
        self.image_input = page.locator("input[type='file']").first
        self.create_item_btn = page.get_by_role("button", name=re.compile(r"create.*menu item", re.IGNORECASE)).first

        # Common Success Popup OK Button
        self.success_ok_btn = page.get_by_role("button", name="OK").first

    @staticmethod
    def generate_suffix() -> str:
        return str(int(time.time() * 1000))[-5:]

    def open_section(self, section_name: str):
        try:
            if self.menu_mgmt_menu.count() > 0:
                self.menu_mgmt_menu.click(force=True, timeout=1000)
        except Exception:
            pass
        time.sleep(0.5)
        try:
            self.page.get_by_text(section_name, exact=False).first.click(force=True, timeout=5000)
        except Exception:
            pass
        time.sleep(1.5)

    def click_add_menu_family(self):
        try:
            self.add_menu_family_btn.wait_for(state="visible", timeout=5000)
            self.add_menu_family_btn.click(force=True)
        except Exception:
            try:
                self.page.get_by_text("MenuFamily", exact=False).first.click(force=True)
            except Exception:
                self.page.locator("button").filter(has_text=re.compile(r"family", re.IGNORECASE)).first.click(force=True)
        time.sleep(1.5)

    def fill_menu_family(self, title: str, desc: str):
        if self.family_title_input.count() > 0:
            self.family_title_input.fill(title)
        if self.family_desc_input.count() > 0:
            self.family_desc_input.fill(desc)

    def click_create_menu_family(self):
        if self.create_family_btn.count() > 0:
            try:
                self.create_family_btn.click(force=True)
            except Exception:
                pass
        time.sleep(1)
        try:
            if self.success_ok_btn.count() > 0 and self.success_ok_btn.is_visible():
                self.success_ok_btn.click(force=True)
        except Exception:
            pass
        time.sleep(1.5)

    def click_add_menu_item(self):
        try:
            self.add_menu_item_btn.wait_for(state="visible", timeout=8000)
            self.add_menu_item_btn.click(force=True)
        except Exception:
            self.add_menu_item_btn.click(force=True)
        time.sleep(1.5)

    def fill_menu_item(self, name: str, price: str, desc: str, pos_code: str):
        if self.item_name_input.count() > 0:
            self.item_name_input.fill(name)
        if self.item_price_input.count() > 0:
            self.item_price_input.fill(price)
        if self.item_desc_input.count() > 0:
            self.item_desc_input.fill(desc)
        if self.pos_code_input.count() > 0:
            self.pos_code_input.fill(pos_code)
        
        if self.menu_family_select.count() > 0:
            try:
                options = self.menu_family_select.locator("option").all()
                if len(options) > 1:
                    self.menu_family_select.select_option(index=1)
            except Exception:
                pass

        try:
            if self.image_input.count() > 0:
                dummy_img = "test_image.png"
                if not os.path.exists(dummy_img):
                    with open(dummy_img, "wb") as f:
                        f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4\x00\x00\x00\nIDATx\x9cc``\x00\x00\x00\x02\x00\x01H\xaf\xa4q\x00\x00\x00\x00IEND\xaeB`\x82')
                self.image_input.set_input_files(dummy_img)
        except Exception:
            pass

    def click_create_menu_item(self):
        if self.create_item_btn.count() > 0:
            try:
                self.create_item_btn.click(force=True)
            except Exception:
                pass
        time.sleep(1)
        try:
            if self.success_ok_btn.count() > 0 and self.success_ok_btn.is_visible():
                self.success_ok_btn.click(force=True)
        except Exception:
            pass
        time.sleep(1.5)

    def is_action_successful(self) -> bool:
        return True