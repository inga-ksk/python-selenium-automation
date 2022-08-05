# Created by Inga at 19.07.2022
Feature: Test scenario for bestsellers page
  # This test case is aimed at verifying the number of bestsellers' link number

  Scenario: User sees 5 links on bestsellers' page
    Given Open Amazon main page
    When Click on bestsellers link
    Then Verify 5 bestseller links are shown
    And Click on each top link and Verify that correct page opens