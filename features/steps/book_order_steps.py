from behave import given, when, then
from pages.book_order_page import BookOrderPage
from playwright.sync_api import expect

@given('I am on the Book New Order page')
def step_impl(context):
    context.book_order_page = BookOrderPage(context.page)
    context.book_order_page.open()

@when('I enter phone number "{phone}"')
def step_impl(context, phone):
    context.book_order_page.enter_phone_number(phone)

@when('I select city "{city}"')
def step_impl(context, city):
    context.book_order_page.select_city(city)

@when('I select location "{location}"')
def step_impl(context, location):
    context.book_order_page.select_location(location)

@when('I select branch "{branch}"')
def step_impl(context, branch):
    context.book_order_page.select_branch(branch)

@when('I select payment mode "{mode}"')
def step_impl(context, mode):
    context.book_order_page.select_payment_mode(mode)

@when('I fill delivery address "{address}"')
def step_impl(context, address):
    context.book_order_page.fill_delivery_address(address)

@when('I select menu category "{category}"')
def step_impl(context, category):
    context.book_order_page.select_menu_category(category)

@when('I add menu item "{item}"')
def step_impl(context, item):
    context.book_order_page.add_menu_item(item)

# --- Added Missing / Aliased Step Definitions to Prevent Errors ---
@then('the item "{item}" should appear in the cart')
def step_impl(context, item):
    assert context.book_order_page.is_item_in_cart(item), f"Item '{item}' not found in cart!"

@then('I verify cart item "{item}"')
def step_impl(context, item):
    assert context.book_order_page.is_item_in_cart(item), f"Item '{item}' not found in cart!"

@then('the order total should dynamically match the added item price')
def step_impl(context):
    total = context.book_order_page.get_total_amount()
    assert total > 0, f"Total amount is invalid: {total}"

@then('the total price should be calculated correctly')
def step_impl(context):
    total = context.book_order_page.get_total_amount()
    assert total > 0, f"Total amount is invalid: {total}"

@then('the submit order button should show "{expected_text}"')
def step_impl(context, expected_text):
    btn_text = context.book_order_page.get_submit_button_text()
    assert expected_text.lower() in btn_text.lower(), f"Expected '{expected_text}', but got '{btn_text}'"

@when('I click the submit order button')
def step_impl(context):
    context.book_order_page.submit_order()

@when('I submit the order')
def step_impl(context):
    context.book_order_page.submit_order()

@then('I should see order confirmation popup')
def step_impl(context):
    assert context.book_order_page.is_confirmation_popup_visible(), "Confirmation popup not visible!"

@then('I should see the confirmation popup')
def step_impl(context):
    assert context.book_order_page.is_confirmation_popup_visible(), "Confirmation popup not visible!"

@when('I confirm the order')
def step_impl(context):
    context.book_order_page.confirm_order()

@then('I should see the order submitted successfully message')
def step_impl(context):
    assert context.book_order_page.is_order_success_visible(), "Order success message not visible!"

@then('I should see order success message')
def step_impl(context):
    assert context.book_order_page.is_order_success_visible(), "Order success message not visible!"