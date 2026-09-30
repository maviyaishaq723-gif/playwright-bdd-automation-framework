Feature: Tenant Admin Login
  As a Tenant Admin
  I want to log into the HDS system
  So that I can access the Tenant Admin dashboard

  Scenario: Login with valid credentials
    Given I am on the HDS login page
    When I enter username "Bandukhan" and password "Test@123"
    And I click the login button
    Then I should see the Tenant Admin dashboard

  Scenario: Login with invalid password
    Given I am on the HDS login page
    When I enter username "Bandukhan" and password "wrongpass"
    And I click the login button
    Then I should stay on the login page

  Scenario: Login with invalid username
    Given I am on the HDS login page
    When I enter username "invaliduser123" and password "anypass"
    And I click the login button
    Then I should stay on the login page

  Scenario: Login with empty username and password
    Given I am on the HDS login page
    When I leave the username and password fields blank
    And I click the login button
    Then I should stay on the login page

  Scenario: Login with username filled and password empty
    Given I am on the HDS login page
    When I enter username "Bandukhan" only, leaving password blank
    And I click the login button
    Then I should stay on the login page