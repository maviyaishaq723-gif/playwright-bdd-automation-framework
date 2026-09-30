from behave import given, when, then
from pages.reports_page import ReportsPage

@given('I am logged in and on the Dashboard')
def step_impl(context):
    if not hasattr(context, 'reports_page'):
        context.reports_page = ReportsPage(context.page)
    context.reports_page.open_dashboard()

@given('I navigate to "{report_type}" page')
def step_impl(context, report_type):
    if not hasattr(context, 'reports_page'):
        context.reports_page = ReportsPage(context.page)
    context.reports_page.navigate_to_sub_report(report_type)

@when('I select city "{city}" in report')
def step_impl(context, city):
    context.reports_page.select_report_filter("City", city)

@when('I select branch "{branch}" in report')
def step_impl(context, branch):
    context.reports_page.select_report_filter("Branch", branch)

@when('I select payment mode "{payment_mode}" in report')
def step_impl(context, payment_mode):
    context.reports_page.select_report_filter("Payment Mode", payment_mode)

@when('I select category "{category}" in report')
def step_impl(context, category):
    context.reports_page.select_report_filter("Category", category)

@when('I set date range from "6 months ago" to "today"')
def step_impl(context):
    context.reports_page.set_6_months_date_range()

@when('I click on Get Report button')
def step_impl(context):
    context.reports_page.click_get_report()

@then('the report should be displayed or show valid status')
def step_impl(context):
    assert context.reports_page.is_report_generated_or_handled(), "Report generation failed!"

@then('I extract and verify the Excel download file')
def step_impl(context):
    is_downloaded = context.reports_page.export_and_verify_excel()
    assert is_downloaded, "Excel file extract/download fail ho gaya!"