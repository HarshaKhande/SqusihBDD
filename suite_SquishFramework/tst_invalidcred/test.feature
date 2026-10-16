Feature: Login functionality


  Scenario: Invalid Login
    Given the browser is launched
    When I enter invalid credentials
    And I click login button
    Then error message should be displayed