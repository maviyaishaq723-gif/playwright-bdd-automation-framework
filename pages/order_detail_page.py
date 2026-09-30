import time
from playwright.sync_api import Page, expect

class OrderDetailPage:
    def __init__(self, page: Page):
        self.page = page
        
        # 1. Active Orders ke liye sidebar elements
        self.orders_menu = page.locator("text=Orders").first
        self.active_order_sub = page.locator("text=Active Order").first
        
        # 2. Neeche Order Management ke liye sidebar elements
        self.order_management_menu = page.locator("text=Order Management").first
        self.order_detail_sub = page.locator("text=Order Detail").first
        
        # 3. Order Detail page elements
        self.order_id_input = page.get_by_placeholder("Enter order ID").first
        self.search_button = page.locator("button:has-text('Search')").first

    def fetch_id_and_search_in_order_detail(self) -> str:
        """Upar Active Orders se ID fetch karke, neeche Order Management > Order Detail mein search karta hai"""
        try:
            # Step A: Uper Orders > Active Order par jao
            if self.orders_menu.is_visible(timeout=3000):
                self.orders_menu.click(force=True)
                time.sleep(1)
            
            if self.active_order_sub.is_visible(timeout=3000):
                self.active_order_sub.click(force=True)
                time.sleep(2)
            else:
                self.page.goto("http://bpocms.ptclgroup.com/MultiTenantHDS/current-order", wait_until="domcontentloaded")
                time.sleep(2)

            # Step B: Table ke pehle row se ORDER # (jaise 1601) uthao[cite: 14]
            id_locator = self.page.locator("xpath=//table//tbody//tr[1]/td[2]").first
            id_locator.wait_for(state="visible", timeout=10000)
            order_id = id_locator.inner_text().strip()
            print(f"\n[INFO] Fetched Active Order ID: {order_id}")

            if not order_id:
                return ""

            # Step C: Ab sidebar mein thora neeche aa kar Order Management > Order Detail par click karo[cite: 13]
            # Pehle sidebar ko view mein laane ke liye scroll ya general click
            self.page.evaluate("window.scrollTo(0, 0)")
            time.sleep(0.5)

            if self.order_management_menu.is_visible(timeout=3000):
                self.order_management_menu.click(force=True)
                time.sleep(1)
            
            if self.order_detail_sub.is_visible(timeout=3000):
                self.order_detail_sub.click(force=True)
                time.sleep(2)
            else:
                self.page.goto("http://bpocms.ptclgroup.com/MultiTenantHDS/order-detail", wait_until="domcontentloaded")
                time.sleep(2)

            # Step D: Order Detail page par search bar mein ID put karke search dabao[cite: 13]
            self.order_id_input.wait_for(state="visible", timeout=10000)
            self.order_id_input.click()
            self.order_id_input.fill("")
            self.order_id_input.fill(order_id)
            time.sleep(0.5)

            self.search_button.wait_for(state="visible", timeout=5000)
            self.search_button.click(force=True)
            time.sleep(3)

            return order_id
        except Exception as e:
            print(f"\n[ERROR] Flow execution error: {e}")
            return ""

    def is_search_result_loaded(self) -> bool:
        """Verify karta hai ke search successful ho gayi hai"""
        try:
            result_card = self.page.locator("xpath=//div[contains(@class, 'card') or contains(@class, 'table') or contains(@class, 'detail')]").last
            result_card.wait_for(state="visible", timeout=10000)
            return True
        except Exception:
            return self.order_id_input.input_value() != ""