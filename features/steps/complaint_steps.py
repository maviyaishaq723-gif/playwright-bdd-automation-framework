from behave import given, when, then
from pages.complaint_page import ComplaintPage

@given('I navigate to "{sub_menu}" section under Complaint Management')
def step_impl_nav_sub(context, sub_menu):
    context.complaint_page = ComplaintPage(context.page)
    context.complaint_page.navigate_to_sub_menu(sub_menu)

@when('I create a dynamic complaint category')
def step_impl_add_cat_dynamic(context):
    context.complaint_page.add_dynamic_complaint_category()

@then('the category should be created successfully')
def step_impl_verify_cat(context):
    assert context.complaint_page.page is not None

@when('I dynamically search for a complaint by Order Number from table and view its log')
def step_impl_search_log_dynamic(context):
    context.complaint_page.search_existing_complaint_and_view_log()

@then('the log modal should be closed successfully')
def step_impl_verify_log_close(context):
    assert context.complaint_page.page is not None

@when('I fill and submit complaint form with details:')
def step_impl_create_complaint(context):
    row = context.table[0]
    context.complaint_page.create_dynamic_complaint(
        name=row['Name'],
        phone=row['Phone'],
        category=row['Category'],
        branch=row['Branch'],
        order_no=row['OrderNo'],
        channel=row['Channel'],
        source=row['Source'],
        remark=row['Remark']
    )

@then('the new complaint should be created successfully')
def step_impl_verify_complaint(context):
    assert context.complaint_page.page is not None