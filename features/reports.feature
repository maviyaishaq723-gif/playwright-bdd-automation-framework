Feature: Reports Module Verification

  Scenario Outline: Verify filter and generation for various reports with 6 months date range
    Given I navigate to "<ReportType>" page
    When I select city "<City>" in report
    And I select branch "<Branch>" in report
    And I select payment mode "<PaymentMode>" in report
    And I set date range from "6 months ago" to "today"
    And I click on Get Report button
    Then the report should be displayed or show valid status
    And I extract and verify the Excel download file

    Examples:
      | ReportType       | City    | Branch         | PaymentMode     |
      | Sales Report     | All City| All Branches   | All Payment Mode|
      | Cancelled Orders | All City| All Branches   | All Payment Mode|

  Scenario: Verify Complaints Report filters and export with 6 months date range
    Given I navigate to "Complaints Report" page
    When I select category "Late Delivery" in report
    And I set date range from "6 months ago" to "today"
    And I click on Get Report button
    Then the report should be displayed or show valid status
    And I extract and verify the Excel download file