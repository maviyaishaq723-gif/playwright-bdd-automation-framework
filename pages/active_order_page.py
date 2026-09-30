class ActiveOrderPage:
    def __init__(self, page):
        self.page = page

    def get_row(self, order_id):
        return self.page.locator("tbody tr").filter(has_text=str(order_id))

    def _ensure_no_modal(self):
        overlay = self.page.locator('div[data-state="open"].fixed.inset-0')
        if overlay.count() > 0:
            self.page.keyboard.press("Escape")
            self.page.wait_for_timeout(500)

    def get_status_or_none(self, order_id):
        self._ensure_no_modal()
        self.page.wait_for_timeout(1500)
        row = self.get_row(order_id)
        if row.count() == 0:
            return None
        return row.locator("td").nth(3).inner_text()

    def get_status(self, order_id):
        status = self.get_status_or_none(order_id)
        assert status is not None, f"Order {order_id} not found in the table"
        return status

    def get_rider(self, order_id):
        self._ensure_no_modal()
        self.page.wait_for_timeout(1500)
        return self.get_row(order_id).locator("td").nth(6).inner_text()

    def is_success_toast_visible(self):
        return self.page.get_by_text("successfully", exact=False).first.is_visible()

    def click_details(self, order_id):
        self._ensure_no_modal()
        self.get_row(order_id).locator('button[title="Details"]').click()
        self.page.wait_for_timeout(500)

    def click_update_status(self, order_id):
        self._ensure_no_modal()
        self.get_row(order_id).locator('button[title="Update Status"]').click()
        self.page.wait_for_timeout(500)

    def click_assign_order(self, order_id):
        self._ensure_no_modal()
        self.get_row(order_id).locator('button[title="Assign Order"]').click()
        self.page.wait_for_timeout(500)

    def click_accept(self):
        self.page.get_by_role("button", name="Accept").click()
        self.page.wait_for_timeout(2000)

    def select_new_status(self, status_text):
        self.page.locator('[role="dialog"]').get_by_role("combobox").click()
        self.page.wait_for_timeout(500)
        self.page.get_by_role("option", name=status_text).click()
        self.page.wait_for_timeout(500)

    def enter_notes(self, notes_text):
        self.page.get_by_placeholder("Enter notes").fill(notes_text)

    def click_update_confirm(self):
        self.page.get_by_role("button", name="Update", exact=True).click()
        self.page.wait_for_timeout(2000)

    def select_rider(self, rider_name):
        self.page.locator('[role="dialog"]').get_by_role("combobox").click()
        self.page.wait_for_timeout(500)
        self.page.get_by_role("option", name=rider_name).click()
        self.page.wait_for_timeout(500)

    def click_assign_rider_confirm(self):
        self.page.get_by_role("button", name="Assign Rider").click()
        self.page.wait_for_timeout(2000)

    def order_items_heading_visible(self):
        return self.page.get_by_role("heading", name="Order Items").first.is_visible()

    def close_modal(self):
        self.page.keyboard.press("Escape")
        self.page.wait_for_timeout(500)