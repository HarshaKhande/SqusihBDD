Feature: Login functionality

    Verify the login functionality for the different user types and verfiy the forgot password functionality


   @smoke
   Scenario: Verify the login scenario for a single user
        Given QA Environment is up and running
        When user enters "admin" and "admin123"
        And user clicks on login button
        Then user is navigated to home page