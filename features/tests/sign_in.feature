Feature: SignIn Test

#  Scenario: Logged out user can sign in
#    Given Open Target main page
#    When Click Sign In
#    And From side navigation menu, click Sign In
#    Then Verify Sign into your Target account seen
#
  Scenario: Authorised user can log in
    Given Open Target main page
    When Click Sign In
    And From side navigation menu, click Sign In
    And Input email and password on SighIn page
    And Click Sign In on Sign In page
    Then Verify user is logged in
