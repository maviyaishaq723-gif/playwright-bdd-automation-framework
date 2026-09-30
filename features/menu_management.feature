@menu_management_module
Feature: Menu Management Professional Flow
  As an admin of Bandu Khan tenant
  I want to manage menu categories and menu items robustly
  So that restaurant ordering and storefront catalog remain updated

  Background:
    Given I navigate to Menu Management section

  Scenario: Create a new Menu Family successfully
    Given I am on the Menu Categories page
    When I click "Add MenuFamily" button
    And I fill the create menu family form with unique details
    And I click "Create Menu Family" button
    Then the menu family creation should be successful

  Scenario: Create a new Menu Item successfully
    Given I am on the Menu Items page
    When I click "Add Menu" button
    And I fill the create menu item form with unique details and role/family
    And I click "Create Menu Item" button
    Then the menu item creation should be successful