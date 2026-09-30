from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.active_order_page import ActiveOrderPage
from pages.user_management_page import UserManagementPage

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.logged_in = False
    context.shared_page = None

def before_feature(context, feature):
    # Har feature ke liye shared page use karna taaki baar baar browser na khule
    if not context.shared_page or context.shared_page.is_closed():
        context.shared_page = context.browser.new_page()
    context.page = context.shared_page

    # Agar login nahi hua toh sabse pehle login perform karein
    if not context.logged_in:
        login_page = LoginPage(context.page)
        login_page.open()
        login_page.login("Bandukhan", "Test@123")
        try:
            context.page.wait_for_url("**/dashboard", timeout=15000)
        except Exception:
            pass
        context.page.wait_for_timeout(2000)
        context.logged_in = True

    # Agar feature mein active_order tag hai toh orders section mein jayein
    if "active_order" in feature.tags:
        try:
            context.page.click("text=Orders")
            context.page.wait_for_timeout(500)
            context.page.click("text=Active Order")
            context.page.wait_for_url("**/current-order", timeout=15000)
            context.page.wait_for_timeout(2000)
            context.active_order_page = ActiveOrderPage(context.page)
            context.order_id = context.page.locator("tbody tr").first.locator("td").nth(1).inner_text()
        except Exception:
            pass

def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
    pass

def after_feature(context, feature):
    pass

def after_all(context):
    if hasattr(context, "shared_page") and context.shared_page and not context.shared_page.is_closed():
        context.shared_page.close()
    if getattr(context, "browser", None):
        context.browser.close()
    if getattr(context, "playwright", None):
        context.playwright.stop()