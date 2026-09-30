@locations_module
Feature: Locations Management Professional Flow

  Background:
    Given I navigate to Locations section

  Scenario: Create a new Branch successfully
    Given I am on the Add Branch page
    When I fill the create branch form with details
    And I click "Create Branch" button
    Then the branch creation should be successful

  Scenario: Create a new Branch Location successfully
    Given I am on the Add Branch Location page
    When I fill the create branch location form with details
    And I click "Save Branch Location" button
    Then the branch location creation should be successful