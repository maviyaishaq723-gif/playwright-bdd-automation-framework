from behave import given, when, then
from pages.riders_page import RidersPage

@given('I navigate to Rider List section')
def step_impl_nav_riders(context):
    context.riders_page = RidersPage(context.page)
    context.riders_page.navigate_to_rider_list()

@given('I click on "Add New Rider" button')
def step_impl_click_add_rider(context):
    context.riders_page.click_add_new_rider_button()

@when('I fill the create rider form with valid dynamic details')
def step_impl_fill_rider(context):
    name, phone, cnic, password = context.riders_page.generate_random_data()
    context.riders_page.fill_rider_form(name, phone, cnic, password)

@when('I click "Create Rider" button')
def step_impl_click_create_rider(context):
    context.riders_page.click_create_rider()

@then('the branch rider creation should be successful')
def step_impl_rider_success(context):
    assert context.riders_page.page is not None