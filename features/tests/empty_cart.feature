Feature: Test Scenario for Cart state

  Scenario: User sees empty cart if no items added
    Given Open Amazon main page
    When Click on the cart icon
    Then Verify product count equals to 0
