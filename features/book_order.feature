@order_flow @book_order
Feature: Book Order Complete Module Automation

  Background:
    Given I am on the Book New Order page

  Scenario: Verify initial state of empty cart and submit button
    Then the submit order button should show "Submit Order (0 items)"

  Scenario: Complete End-to-End Order Booking and Verification Flow
    When I enter phone number "03165562895"
    And I select city "Lahore"
    And I select location "Guldberg 2 Lahore-Lahore"
    And I select branch "Bandu Khan Lahore - Guldberg h2 lahore"
    And I select payment mode "Cash on Delivery"
    And I fill delivery address "House 123, Street 5, Gulberg 2, Lahore"
    And I select menu category "All Menu"
    And I add menu item "Seekh Kabab"
    Then the submit order button should show "Submit Order (1 items)"
    And the item "Seekh Kabab" should appear in the cart
    And the order total should dynamically match the added item price
    When I click the submit order button
    Then I should see order confirmation popup
    When I confirm the order
    Then I should see the order submitted successfully message