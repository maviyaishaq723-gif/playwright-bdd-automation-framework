@riders_module
Feature: Branch Riders Management Professional Flow

  Scenario: Create a new Branch Rider successfully
    Given I navigate to Rider List section
    And I click on "Add New Rider" button
    When I fill the create rider form with valid dynamic details
    And I click "Create Rider" button
    Then the branch rider creation should be successful