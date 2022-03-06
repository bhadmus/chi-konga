Feature: Testing Konga's Login
  As a user, I should be able to login.

  Scenario: User should be able to login with username and password
    Given I am on konga site
    When I click the login link
    And I fill in the username
    And I fill in the password
    And I click the login button
    Then I should see the homepage
