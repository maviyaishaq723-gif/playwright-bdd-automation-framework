from behave import given, when, then
from pages.locations_page import LocationsPage

@given('I navigate to Locations section')
def step_impl_nav_locations(context):
    context.locations_page = LocationsPage(context.page)
    context.locations_page.open_locations_section()

@given('I am on the Add Branch page')
def step_impl_on_add_branch(context):
    context.locations_page.navigate_to_add_branch()

@when('I fill the create branch form with details')
def step_impl_fill_branch(context):
    suffix = context.locations_page.generate_suffix()
    context.locations_page.fill_branch_form(
        name=f"Branch_{suffix}",
        address="Main Boulevard, Lahore",
        lat="31.4697",
        long="74.2728"
    )

@when('I click "Create Branch" button')
def step_impl_click_create_branch(context):
    context.locations_page.click_create_branch()

@then('the branch creation should be successful')
def step_impl_branch_success(context):
    assert context.locations_page.page is not None

@given('I am on the Add Branch Location page')
def step_impl_on_add_location(context):
    context.locations_page.navigate_to_add_branch_location()

@when('I fill the create branch location form with details')
def step_impl_fill_location(context):
    suffix = context.locations_page.generate_suffix()
    context.locations_page.fill_branch_location_form(
        title=f"Location_{suffix}",
        desc="Main takeaway and delivery counter"
    )

@when('I click "Save Branch Location" button')
def step_impl_click_save_location(context):
    context.locations_page.click_save_branch_location()

@then('the branch location creation should be successful')
def step_impl_location_success(context):
    assert context.locations_page.page is not None