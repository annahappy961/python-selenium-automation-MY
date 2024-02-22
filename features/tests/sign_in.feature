Feature: SignIn Test

  Scenario: Logged out user can sign in
    Given Open Target main page
    When Click Sign In
    And From side navigation menu, click Sign In
    Then Verify Sign into your Target account seen
