@order_flow @active_order
Feature: Active Order Management
  As a tenant admin
  I want to manage newly placed orders end-to-end
  So that orders move correctly from placement to delivery

  Scenario: Newly booked order appears with status "New Order"
    Then the order status should be "New Order"

  Scenario: View order details of the new order
    When I click the details button
    Then the order detail popup should show the order items
    And I close the popup

  Scenario: Accept the new order
    When I click the update status button
    And I click the accept button
    Then the order status should change to "Received"

  Scenario: Move the order to Dispatched
    Given the order status is "Received"
    When I click the update status button
    And I select "Dispatched" as the new status
    And I enter "Order picked up for delivery" in the notes field
    And I click the update button
    Then the order status should change to "Dispatched"

  Scenario: Assign a rider to the dispatched order
    Given the order status is "Dispatched"
    When I click the assign order button
    And I select rider "Salman Lahore" from the rider list
    And I click the assign rider button
    Then the rider column should show "Salman Lahore"

  Scenario: Mark the order as Delivered
    Given the order status is "Dispatched"
    When I click the update status button
    And I select "Delivered" as the new status
    And I enter "Order delivered successfully" in the notes field
    And I click the update button
    Then the order status should change to "Delivered"