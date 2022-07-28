# Created by Inga at 25.07.2022
Feature: Test scenario for search functionality

  Scenario: User can see name and image of product when searching on Amazon
    Given Open Amazon main page
    When Input  iron  into Amazon search field
    And Click on Amazon search icon
    Then Product results for iron are shown on Amazon
    And Every product has name
    And Every product has image