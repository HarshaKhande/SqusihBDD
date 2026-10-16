Feature: Login functionality

  Scenario Outline: Login with multiple users
    Given the login page is open
    When I login with username <username> and password <password>
    Then the login result should be <expected>

    Examples:
      | username | password | expected |
      | admin    | admin123 | Success  |
      | tester   | test123  | Success  |
      | wrong    | wrong123 | Failure  |
