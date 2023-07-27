# Created by stephenokonkwo at 7/14/23
Feature: cureskin search result test cases

  @smoke
  Scenario: Search results shows the right result
    Given Open Main page
    When From Header Page, click "Search"
    And Search for SPF
    And Click on product
    Then Verify the results have SPF
