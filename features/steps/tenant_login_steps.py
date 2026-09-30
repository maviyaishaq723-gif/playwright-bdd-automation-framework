from behave import then

@then('I should see the Tenant Admin dashboard')
def step_verify_tenant_admin_dashboard(context):
    try:
        context.page.wait_for_url("**/admin-dashboard", timeout=15000)
    except Exception:
        pass
    current_url = context.page.url
    assert "admin-dashboard" in current_url, f"Expected Tenant Admin dashboard URL, got: {current_url}"
    context.page.wait_for_timeout(3000)