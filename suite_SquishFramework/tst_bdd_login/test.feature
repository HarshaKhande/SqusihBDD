Feature: Login functionality

  Scenario: Login with single user
    Given the login page is open
    When I login with username admin and password admin123
	Then the login result should be Success



