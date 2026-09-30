import time
import re
from playwright.sync_api import Page

class LocationsPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Sidebar Dropdown Menu Locators
        self.locations_sidebar_menu = page.locator("a:has-text('Locations'), li:has-text('Locations')").first
        self.add_branch_sidebar_item = page.locator("a[href*='add-branch'], a:has-text('Add Branch'), a:has-text('Branches')").first
        self.add_location_sidebar_item = page.locator("a[href*='branch-location'], a:has-text('Branch Location'), a:has-text('Add Location')").first
        
        # Page Action Buttons
        self.add_new_btn = page.locator("a:has-text('Add Branch'), button:has-text('Add Branch')").first
        self.add_location_btn = page.locator("a:has-text('Add Location'), button:has-text('Add Location')").first

        # Branch Form Fields
        self.branch_name_input = page.locator("input[placeholder*='branch name' i]").first
        self.branch_address_input = page.locator("input[placeholder*='branch address' i]").first
        self.city_select = page.locator("select").first
        self.latitude_input = page.locator("input[placeholder*='24.8607' i], input[placeholder*='latitude' i]").first
        self.longitude_input = page.locator("input[placeholder*='67.0011' i], input[placeholder*='longitude' i]").first
        self.create_branch_btn = page.get_by_role("button", name=re.compile(r"create.*branch", re.IGNORECASE)).first

        # Branch Location Form Fields
        self.select_branch_dropdown = page.locator("select").first
        self.location_title_input = page.locator("input[placeholder*='location title' i], input[placeholder*='title' i]").first
        self.location_desc_input = page.locator("input[placeholder*='description' i], textarea[placeholder*='description' i]").first
        self.save_branch_location_btn = page.get_by_role("button", name=re.compile(r"save.*branch.*location", re.IGNORECASE)).first
        
        # Popup OK Button
        self.success_ok_btn = page.get_by_role("button", name="OK").first

    @staticmethod
    def generate_suffix() -> str:
        return str(int(time.time() * 1000))[-5:]

    def open_locations_section(self):
        if self.locations_sidebar_menu.is_visible():
            self.locations_sidebar_menu.click()
            time.sleep(1)

    def navigate_to_add_branch(self):
        self.open_locations_section()
        
        if self.add_branch_sidebar_item.is_visible():
            self.add_branch_sidebar_item.click()
            time.sleep(1.5)
            
        if self.add_new_btn.is_visible():
            self.add_new_btn.click()
            time.sleep(1)

    def fill_branch_form(self, name: str, address: str, lat: str, long: str):
        self.branch_name_input.wait_for(state="visible", timeout=10000)
        self.branch_name_input.fill(name)
        self.branch_address_input.fill(address)
        
        if self.city_select.count() > 0:
            try:
                options = self.city_select.locator("option").all()
                if len(options) > 1:
                    self.city_select.select_option(index=1)
            except Exception:
                pass

        self.latitude_input.fill(lat)
        self.longitude_input.fill(long)

    def click_create_branch(self):
        self.create_branch_btn.click(force=True)
        time.sleep(1)
        try:
            if self.success_ok_btn.is_visible(timeout=3000):
                self.success_ok_btn.click(force=True)
        except Exception:
            pass
        time.sleep(1.5)

    def navigate_to_add_branch_location(self):
        self.open_locations_section()
        
        # 1. Sidebar se Location screen par jana
        if self.add_location_sidebar_item.is_visible():
            self.add_location_sidebar_item.click()
            time.sleep(1.5)

        # 2. Page par moujood Red '+ Add Location' button par click karna
        if self.add_location_btn.is_visible():
            self.add_location_btn.click()
            time.sleep(1.5)

    def fill_branch_location_form(self, title: str, desc: str):
        self.location_title_input.wait_for(state="visible", timeout=10000)
        
        if self.select_branch_dropdown.count() > 0:
            try:
                options = self.select_branch_dropdown.locator("option").all()
                if len(options) > 1:
                    self.select_branch_dropdown.select_option(index=1)
            except Exception:
                pass

        self.location_title_input.fill(title)
        self.location_desc_input.fill(desc)

    def click_save_branch_location(self):
        self.save_branch_location_btn.click(force=True)
        time.sleep(1)
        try:
            if self.success_ok_btn.is_visible(timeout=3000):
                self.success_ok_btn.click(force=True)
        except Exception:
            pass
        time.sleep(1.5)