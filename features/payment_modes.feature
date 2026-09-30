@payment_modes_module
Feature: Payment Modes Management Professional Flow

  Scenario: Create a new Payment Mode successfully
    Given I navigate to Payment Modes section
    And I click on "Add Payment Mode" button
    When I fill the create payment mode form with details
    And I click "Create Payment Mode" button
    Then the payment mode creation should be successful