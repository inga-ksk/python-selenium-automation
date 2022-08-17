# Created by Inga at 16.08.2022
Feature: This is a test case covering select and hover

  Scenario: Scenario: User can select and search in department
    Given Open Amazon main page
    When Select department by value
    And Input tomatoes into Amazon search field and click search
    Then Verify correct department is selected

  Scenario: User can hover over New Arrivals and sees the deals
    Given Open Amazon product page
    When Hover over New Arrivals
    Then User sees the deals