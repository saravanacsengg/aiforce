Feature: Login Functionality Test

  Scenario: Valid Login
    Given User is on the login page
    When User enters valid credentials
    And User clicks on the login button
    Then User should be redirected to the home page
    And Page title should contain "Swag Labs"

  Scenario: Invalid Login
    Given User is on the login page
    When User enters invalid credentials
    And User clicks on the login button
    Then An error message starting with "Epic sadface" should be displayed