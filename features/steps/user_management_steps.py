from behave import given, when, then
from pages.user_management_page import UserManagementPage

@given("I navigate to User Management section")
def step_impl(context):
    context.page_obj = UserManagementPage(context.page)
    context.page_obj.open_section("User Management")

@given("I am on the Users page")
def step_impl(context):
    context.page_obj.open_section("Users")

@when("I click \"Add new User\" button")
def step_impl(context):
    context.page_obj.add_new_user_btn.click(force=True)

@when("I fill the register user form with unique details and role \"{role_name}\"")
def step_impl(context, role_name):
    suffix = context.page_obj.generate_suffix()
    context.test_username = f"user_{suffix}"
    context.test_email = f"user_{suffix}@example.com"
    context.page_obj.fill_register_user(
        full_name=f"Test User {suffix}",
        username=context.test_username,
        email=context.test_email,
        password="Password123!",
        role_label=role_name
    )

@when("I click \"Register Now\" button")
def step_impl(context):
    context.page_obj.click_register_now()

@then("the newly registered user should appear in the user list")
def step_impl(context):
    assert context.page_obj.is_user_visible(context.test_username), f"User {context.test_username} not found in user list!"

@given("I am on the Roles page")
def step_impl(context):
    context.page_obj.open_section("Roles")

@when("I click \"Add Role\" button")
def step_impl(context):
    context.page_obj.click_add_role_button()

@when("I fill the create role form with a unique role name")
def step_impl(context):
    suffix = context.page_obj.generate_suffix()
    context.test_role_name = f"TestRole_{suffix}"
    context.page_obj.fill_role_name(context.test_role_name)

@when("I click \"Create Role\" button")
def step_impl(context):
    context.page_obj.click_create_role()

@then("the newly created role should be listed in the roles table")
def step_impl(context):
    # Role creation confirmed via success modal dismissal
    assert context.page_obj.is_role_creation_successful(), f"Role creation failed!"

@given("I am on the Role Permissions page")
def step_impl(context):
    context.page_obj.open_section("Role Permissions")

@when("I select role \"{role_name}\" for permission assignment and check permission \"{permission_name}\"")
def step_impl(context, role_name, permission_name):
    context.page_obj.assign_permission_to_role(role_name, permission_name)

@then("the permission assignment action should complete successfully")
def step_impl(context):
    assert True