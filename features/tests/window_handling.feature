# Created by Inga at 04.08.2022
Feature: Terms and Conditions open in a new tab

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User closes new window
    And User switches back to original window
