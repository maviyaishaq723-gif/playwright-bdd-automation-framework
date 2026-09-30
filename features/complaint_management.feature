@complaint_module
Feature: Complaint Management Complete Module Automation

  Scenario: Add a new Complaint Category with dynamic unique name
    Given I navigate to "Complaint Categories" section under Complaint Management
    When I create a dynamic complaint category
    Then the category should be created successfully

  Scenario: Search existing Complaint by Order Number and view Complaint Logs dynamically
    Given I navigate to "Complaints List" section under Complaint Management
    When I dynamically search for a complaint by Order Number from table and view its log
    Then the log modal should be closed successfully

  Scenario: Create a new Customer Complaint
    Given I navigate to "Create Complaint" section under Complaint Management
    When I fill and submit complaint form with details:
      | Name   | Phone       | Category      | Branch            | OrderNo | Channel  | Source      | Remark                |
      | Maviya | 03315532581 | Late Delivery | Bandu Khan Lahore | AUTO    | Delivery | Call Center | Item quality not good |
    Then the new complaint should be created successfully