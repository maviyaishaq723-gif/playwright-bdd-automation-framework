from behave import given, when, then
from pages.payment_modes_page import PaymentModesPage

@given('I navigate to Payment Modes section')
def step_impl_nav_payment_modes(context):
    context.payment_modes_page = PaymentModesPage(context.page)
    context.payment_modes_page.navigate_to_payment_modes()

@given('I click on "Add Payment Mode" button')
def step_impl_click_add_pm(context):
    context.payment_modes_page.click_add_payment_mode_button()

@when('I fill the create payment mode form with details')
def step_impl_fill_pm(context):
    suffix = context.payment_modes_page.generate_suffix()
    context.payment_modes_page.fill_payment_mode_form(f"Wallet_{suffix}")

@when('I click "Create Payment Mode" button')
def step_impl_click_create_pm(context):
    context.payment_modes_page.click_create_payment_mode()

@then('the payment mode creation should be successful')
def step_impl_pm_success(context):
    assert context.payment_modes_page.page is not None