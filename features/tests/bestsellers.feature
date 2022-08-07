# Created by Inga at 19.07.2022
Feature: Test scenario for bestsellers page
  # This test case is aimed at verifying the number of bestsellers' link number

  Scenario: User sees 5 links on bestsellers' page
    Given Open Amazon Bestsellers
    Then Verify there are 5 links
    And User can click through top links and verify correct page opens