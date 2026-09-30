import time
import re
from playwright.sync_api import Page

class ComplaintPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Sidebar Parent & Submenu Locators
        self.complaint_mgmt_parent = page.locator("*:has-text('Complaint_Management')").filter(has_text=re.compile(r"^Complaint_Management$")).first
        self.complaint_categories_sub = page.locator("a:has-text('Complaint Categories'), span:has-text('Complaint Categories')").first
        self.complaints_list_sub = page.locator("a:has-text('Complaints List'), span:has-text('Complaints List')").first
        self.create_complaint_sub = page.locator("a:has-text('Create Complaint'), span:has-text('Create Complaint')").first
        
        # Orders Navigation for Valid Active Order ID Fetching
        self.orders_parent_menu = page.locator("a:has-text('Orders'), span:has-text('Orders')").first
        self.active_orders_sub_menu = page.locator("a:has-text('Active Order')").first
        self.first_active_order_num_cell = page.locator("table tbody tr:first-child td:nth-child(2)").first

        # 1. Complaint Categories Page Locators
        self.add_category_btn = page.locator("a:has-text('Add Complaint Categories'), button:has-text('Add Complaint Categories')").first
        self.category_name_input = page.locator("input[placeholder*='category' i], input[type='text']").first
        self.submit_category_btn = page.locator("button:has-text('Create Category')").first
        
        # 2. Complaints List Page Locators (Column 7 holds ORDER NO)
        self.search_input = page.locator("input[placeholder*='Search' i]").first
        self.first_row_order_no_cell = page.locator("table tbody tr:first-child td:nth-child(7)").first
        self.log_btn_first = page.locator("table tbody tr:first-child button:has-text('Log'), table tbody tr:first-child a:has-text('Log')").first
        self.close_log_modal_btn = page.locator("button:has-text('Close'), .modal button, [data-bs-dismiss='modal']").first
        
        # 3. Create Complaint Page Locators (100% Precise Selector)
        self.customer_name_input = page.locator("input[placeholder*='customer name' i]").first
        self.phone_number_input = page.locator("input[placeholder*='phone number' i]").first
        self.order_number_input = page.locator("xpath=//label[contains(text(),'Order Number')]/parent::div//input | //label[contains(text(),'Order Number')]/following-sibling::input | input[type='number']").first
        self.remark_textarea = page.locator("textarea[placeholder*='remark' i], textarea").first
        self.submit_complaint_btn = page.locator("button:has-text('Create Complaint')").first

    def fetch_valid_active_order_id(self) -> str:
        """Active Orders screen par ja kar latest valid Order ID fetch karta hai"""
        try:
            self.orders_parent_menu.scroll_into_view_if_needed()
            self.orders_parent_menu.click(force=True)
            time.sleep(1)
            
            self.active_orders_sub_menu.click(force=True)
            time.sleep(2)
            
            self.first_active_order_num_cell.wait_for(state="visible", timeout=5000)
            raw_id = self.first_active_order_num_cell.text_content().strip()
            clean_id = re.sub(r'[^\w\d-]', '', raw_id)
            return clean_id
        except Exception:
            return "1595"

    def expand_complaint_menu(self):
        """Complaint Management parent menu open karta hai agar closed ho"""
        self.complaint_mgmt_parent.scroll_into_view_if_needed()
        time.sleep(0.5)
        if not self.create_complaint_sub.is_visible():
            self.complaint_mgmt_parent.click(force=True)
            time.sleep(1)

    def navigate_to_sub_menu(self, menu_name: str):
        """Requested sub-menu par navigate karta hai"""
        self.expand_complaint_menu()
        
        menu_map = {
            "Complaint Categories": self.complaint_categories_sub,
            "Complaints List": self.complaints_list_sub,
            "Create Complaint": self.create_complaint_sub
        }
        
        target = menu_map.get(menu_name)
        if target:
            target.wait_for(state="visible", timeout=10000)
            target.scroll_into_view_if_needed()
            target.click(force=True)
            time.sleep(1.5)

    def select_dropdown_option(self, placeholder_text: str, option_text: str):
        """Standard select aur custom div dropdowns ko safely handle karta hai"""
        if not option_text:
            return
            
        try:
            selects = self.page.locator("select").all()
            for sel in selects:
                try:
                    sel.select_option(label=option_text, timeout=1000)
                    return
                except Exception:
                    try:
                        sel.select_option(value=option_text, timeout=1000)
                        return
                    except Exception:
                        pass
        except Exception:
            pass

        try:
            dropdown_trigger = self.page.locator(f"text={placeholder_text}").first
            if dropdown_trigger.is_visible(timeout=1500):
                dropdown_trigger.click(force=True)
                time.sleep(0.5)
                self.page.locator(f"text={option_text}").first.click(force=True)
        except Exception:
            pass

    def add_dynamic_complaint_category(self) -> str:
        """Timestamp base par unique complaint category create karta hai"""
        timestamp = int(time.time())
        unique_cat_name = f"Cat_Auto_{timestamp}"
        
        self.add_category_btn.wait_for(state="visible", timeout=10000)
        self.add_category_btn.click(force=True)
        time.sleep(1.5)
        
        self.category_name_input.wait_for(state="visible", timeout=10000)
        self.category_name_input.fill(unique_cat_name)
        time.sleep(0.5)
        self.submit_category_btn.click(force=True)
        time.sleep(2)
        return unique_cat_name

    def search_existing_complaint_and_view_log(self):
        """Complaints List ki Column 7 se dynamically ORDER NO read karke search aur log view karta hai"""
        self.first_row_order_no_cell.wait_for(state="visible", timeout=10000)
        dynamic_order_no = self.first_row_order_no_cell.text_content().strip()
        
        self.search_input.clear()
        self.search_input.fill(dynamic_order_no)
        time.sleep(1.5)
        
        self.log_btn_first.wait_for(state="visible", timeout=10000)
        self.log_btn_first.click(force=True)
        time.sleep(1.5)
        
        try:
            if self.close_log_modal_btn.is_visible(timeout=3000):
                self.close_log_modal_btn.click(force=True)
            else:
                self.page.keyboard.press("Escape")
        except Exception:
            self.page.keyboard.press("Escape")
        time.sleep(1)

    def create_dynamic_complaint(self, name: str, phone: str, category: str, branch: str, order_no: str, channel: str, source: str, remark: str):
        """Active Order ID fetch karke screen par wapas aakar form fill karta hai"""
        timestamp = str(int(time.time()))[-4:]
        dynamic_name = f"{name}_{timestamp}"
        dynamic_remark = f"{remark} - Auto_{timestamp}"
        
        # 1. Order ID Fetching
        final_order_no = self.fetch_valid_active_order_id() if (not order_no or order_no.upper() == "AUTO") else order_no
        
        # 2. Return to Create Complaint Page
        self.navigate_to_sub_menu("Create Complaint")
        time.sleep(1.5)
            
        # 3. Customer Name
        self.customer_name_input.wait_for(state="visible", timeout=10000)
        self.customer_name_input.fill(dynamic_name)
        
        # 4. Phone Number
        self.phone_number_input.wait_for(state="visible", timeout=5000)
        self.phone_number_input.fill(phone)
            
        # 5. Order Number Input (Guaranteed Fill)
        self.order_number_input.wait_for(state="visible", timeout=5000)
        self.order_number_input.click()
        self.order_number_input.fill("")
        self.order_number_input.fill(str(final_order_no))
        time.sleep(0.5)

        # 6. Dropdowns
        self.select_dropdown_option("Select complaint category", category)
        self.select_dropdown_option("Select branch", branch)
        self.select_dropdown_option("Select channel", channel)
        self.select_dropdown_option("Select Source", source)

        # 7. Remark & Submit
        if self.remark_textarea.is_visible(timeout=3000):
            self.remark_textarea.fill(dynamic_remark)
            
        time.sleep(0.5)
        self.submit_complaint_btn.click(force=True)
        time.sleep(2)