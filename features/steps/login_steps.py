import sys
import os
# Ensure project root/pages is discoverable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from behave import given, when, then
from pages.login_page import LoginPage

@given('I am on the HDS login page')
def step_open_login(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open()

@when('I enter username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.login_page.fill_username(username)
    context.login_page.fill_password(password)

@when('I click the login button')
def step_click_login(context):
    context.login_page.click_login()

@then('I should stay on the login page')
def step_verify_stays_on_login(context): 
    # Use load state or URL expectation instead of blind timeout
    context.page.wait_for_load_state("domcontentloaded")
    current_url = context.page.url
    assert "/login" in current_url, f"Expected to stay on login page, got: {current_url}"

@when('I leave the username and password fields blank')
def step_leave_both_blank(context):
    context.login_page.fill_username("")
    context.login_page.fill_password("")

@when('I enter username "{username}" only, leaving password blank')
def step_enter_username_only(context, username):
    context.login_page.fill_username(username)
    context.login_page.fill_password("")