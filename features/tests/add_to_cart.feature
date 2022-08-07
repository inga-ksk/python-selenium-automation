# Created by Inga at 07.08.2022
Feature: Verify the product can be added to cart

  Scenario: Adding to cart
    Given Open Amazon main page
    When Paste washing machine into search field and click search
    And Click on first search result
    And Add product to cart
    And Decline appliance protection plan
    Then 1 item is present in cart
