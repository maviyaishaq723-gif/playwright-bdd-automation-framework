from behave import when, then
from pages.order_detail_page import OrderDetailPage

@when('I fetch the latest order ID from Active Orders and search it in Order Detail')
def step_impl(context):
    page = OrderDetailPage(context.page)
    order_id = page.fetch_id_and_search_in_order_detail()
    assert order_id != "", "Active Orders se ID fetch nahi ho saki!"
    context.searched_order_id = order_id

@then('the order details should be successfully searched and displayed')
def step_impl(context):
    page = OrderDetailPage(context.page)
    assert page.is_search_result_loaded(), "Order detail page par search result load nahi hua!"