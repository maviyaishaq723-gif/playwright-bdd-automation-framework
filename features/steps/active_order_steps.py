from behave import given, when, then

@then('the order status should be "{status}"')
def step_check_status(context, status):
    actual = context.active_order_page.get_status(context.order_id)
    assert actual == status, f"Expected {status}, got {actual}"

@when('I click the details button')
def step_click_details(context):
    context.active_order_page.click_details(context.order_id)

@then('the order detail popup should show the order items')
def step_check_items(context):
    assert context.active_order_page.order_items_heading_visible()

@then('I close the popup')
def step_close_popup(context):
    context.active_order_page.close_modal()

@when('I click the update status button')
def step_click_update_status(context):
    context.active_order_page.click_update_status(context.order_id)

@when('I click the accept button')
def step_click_accept(context):
    context.active_order_page.click_accept()

@given('the order status is "{status}"')
def step_given_status(context, status):
    actual = context.active_order_page.get_status(context.order_id)
    assert actual == status, f"Expected order to be in {status}, but found {actual}"

@when('I select "{status}" as the new status')
def step_select_status(context, status):
    context.active_order_page.select_new_status(status)

@when('I enter "{notes}" in the notes field')
def step_enter_notes(context, notes):
    context.active_order_page.enter_notes(notes)

@when('I click the update button')
def step_click_update(context):
    context.active_order_page.click_update_confirm()

@then('the order status should change to "{status}"')
def step_status_changed(context, status):
    actual = context.active_order_page.get_status_or_none(context.order_id)
    if actual is None:
        assert context.active_order_page.is_success_toast_visible(), \
            f"Order disappeared from list after marking {status}, and no success message found"
    else:
        assert actual == status, f"Expected {status}, got {actual}"

@when('I click the assign order button')
def step_click_assign(context):
    context.active_order_page.click_assign_order(context.order_id)

@when('I select rider "{rider_name}" from the rider list')
def step_select_rider(context, rider_name):
    context.active_order_page.select_rider(rider_name)

@when('I click the assign rider button')
def step_click_assign_rider(context):
    context.active_order_page.click_assign_rider_confirm()

@then('the rider column should show "{rider_name}"')
def step_check_rider(context, rider_name):
    actual = context.active_order_page.get_rider(context.order_id)
    assert rider_name in actual, f"Expected {rider_name}, got {actual}"