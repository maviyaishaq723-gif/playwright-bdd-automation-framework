@user_management_module
Feature: User Management and RBAC Professional Flow
  As an admin of Bandu Khan tenant
  I want to manage users, roles, and permissions robustly
  So that clean system operations and access control are maintained

  Background:
    Given I navigate to User Management section

  Scenario: Register a new user successfully with unique credentials
    Given I am on the Users page
    When I click "Add new User" button
    And I fill the register user form with unique details and role "Cashier"
    And I click "Register Now" button
    Then the newly registered user should appear in the user list

  Scenario: Create a new custom role with unique name
    Given I am on the Roles page
    When I click "Add Role" button
    And I fill the create role form with a unique role name
    And I click "Create Role" button
    Then the newly created role should be listed in the roles table

  Scenario: Assign specific permission to a role successfully
    Given I am on the Role Permissions page
    When I select role "Cashier" for permission assignment and check permission "NewOrder"
    Then the permission assignment action should complete successfully