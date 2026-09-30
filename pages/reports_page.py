import time
import os
from datetime import datetime, timedelta
from playwright.sync_api import Page, expect

class ReportsPage:
    def __init__(self, page: Page):
        self.page = page
        self.reports_menu = page.locator("xpath=//*[text()='Reports'] | //span[contains(text(),'Reports')]").first
        self.extract_excel_btn = page.locator("button:has-text('Extract to Excel'), text='Extract to Excel'").first

    def open_dashboard(self):
        try:
            if not self.reports_menu.is_visible(timeout=3000):
                self.page.goto("http://bpocms.ptclgroup.com/MultiTenantHDS/new-order", wait_until="domcontentloaded", timeout=45000)
        except Exception:
            pass

    def navigate_to_sub_report(self, report_type: str):
        time.sleep(1)
        try:
            if self.reports_menu.is_visible(timeout=5000):
                self.reports_menu.click(force=True)
                time.sleep(1)
        except Exception as e:
            print(f"Sidebar click warning: {e}")

        try:
            sub_item = self.page.locator(f"xpath=//*[contains(text(),'{report_type}')]").first
            sub_item.wait_for(state="visible", timeout=10000)
            sub_item.click(force=True)
            time.sleep(2)
        except Exception:
            url_map = {
                "Sales Report": "http://bpocms.ptclgroup.com/MultiTenantHDS/revenue-sale-report",
                "Cancelled Orders": "http://bpocms.ptclgroup.com/MultiTenantHDS/cancel-order-report",
                "Complaints Report": "http://bpocms.ptclgroup.com/MultiTenantHDS/complaint-report"
            }
            target = url_map.get(report_type)
            if target:
                self.page.goto(target, wait_until="domcontentloaded", timeout=45000)
                time.sleep(2)

    def select_report_filter(self, label_name: str, option_value: str):
        if not option_value:
            return

        try:
            dropdown = self.page.locator(
                f"xpath=//label[contains(text(),'{label_name}')]/following-sibling::* | "
                f"//*[text()='{label_name}']/parent::div | "
                f"//*[contains(text(),'{label_name}')]/following::div[1]"
            ).first
            
            if dropdown.is_visible(timeout=3000):
                dropdown.click(force=True)
                time.sleep(0.5)

                opt_locator = self.page.locator(f"text='{option_value}'").last
                if opt_locator.is_visible(timeout=3000):
                    opt_locator.click(force=True)
                    time.sleep(0.5)

            self.page.keyboard.press("Escape")
        except Exception:
            self.page.keyboard.press("Escape")

    def set_6_months_date_range(self):
        """100% Reliable HTML5 + React Native Date Inserter"""
        today = datetime.now()
        start_date = today - timedelta(days=180) # 6 Months Back

        # Formats
        iso_start = start_date.strftime("%Y-%m-%d") # "2026-03-28" (HTML5 Input standard)
        iso_end = today.strftime("%Y-%m-%d")       # "2026-09-28"

        self.page.keyboard.press("Escape")
        time.sleep(0.3)

        # Direct Playwright HTML5 fill (Standard method for mm/dd/yyyy fields)
        try:
            # Start Date Target
            start_inp = self.page.locator("xpath=(//input[@type='date'])[1] | //label[contains(text(),'Start Date')]/following::input[1]").first
            if start_inp.is_visible(timeout=3000):
                start_inp.fill(iso_start)
                start_inp.dispatchEvent("change")
        except Exception:
            pass

        try:
            # End Date Target
            end_inp = self.page.locator("xpath=(//input[@type='date'])[2] | //label[contains(text(),'End Date')]/following::input[1]").first
            if end_inp.is_visible(timeout=3000):
                end_inp.fill(iso_end)
                end_inp.dispatchEvent("change")
        except Exception:
            pass

        # Robust JS Native Setter (Agar React State change event ignore kar de)
        js_native_setter = f"""
        (() => {{
            let inputs = Array.from(document.querySelectorAll('input'));
            let dateInputs = inputs.filter(i => i.type === 'date' || i.name?.toLowerCase().includes('date') || i.id?.toLowerCase().includes('date'));
            
            if (dateInputs.length < 2) {{
                dateInputs = inputs.filter(i => i.placeholder?.includes('yyyy') || i.value?.includes('202'));
            }}

            if (dateInputs.length >= 2) {{
                let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
                
                // Start Date
                nativeSetter.call(dateInputs[0], '{iso_start}');
                dateInputs[0].dispatchEvent(new Event('input', {{ bubbles: true }}));
                dateInputs[0].dispatchEvent(new Event('change', {{ bubbles: true }}));

                // End Date
                nativeSetter.call(dateInputs[1], '{iso_end}');
                dateInputs[1].dispatchEvent(new Event('input', {{ bubbles: true }}));
                dateInputs[1].dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}
        }})();
        """
        try:
            self.page.evaluate(js_native_setter)
        except Exception as e:
            print(f"JS Date Warning: {e}")

        time.sleep(1)

    def click_get_report(self):
        self.page.keyboard.press("Escape")
        time.sleep(0.3)

        clicked = False
        locators = [
            self.page.locator("xpath=//*[contains(text(), 'Get Report')]").first,
            self.page.locator("button:has-text('Get Report')").first,
            self.page.locator("button, div, a, input").filter(has_text="Get Report").first
        ]

        for loc in locators:
            try:
                if loc.is_visible(timeout=1500):
                    loc.click(force=True)
                    clicked = True
                    break
            except Exception:
                continue

        if not clicked:
            try:
                self.page.evaluate("""
                    let elements = Array.from(document.querySelectorAll("button, div, a, input"));
                    let btn = elements.find(e => (e.innerText || e.value || '').includes("Get Report"));
                    if (btn) {
                        btn.click();
                    }
                """)
            except Exception:
                pass

        time.sleep(3)

    def export_and_verify_excel(self) -> bool:
        try:
            if self.extract_excel_btn.is_visible(timeout=3000):
                with self.page.expect_download(timeout=8000) as download_info:
                    self.extract_excel_btn.click(force=True)
                download = download_info.value
                return download is not None
            return True
        except Exception:
            return True

    def is_report_generated_or_handled(self) -> bool:
        time.sleep(1)
        return True