Feature: Order Detail Automation

  Scenario: Fetch latest order ID from Active Orders and search in Order Detail
    When I fetch the latest order ID from Active Orders and search it in Order Detail
    Then the order details should be successfully searched and displayed